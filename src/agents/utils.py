from langchain_core.messages import BaseMessage, AIMessage
from agents import build_agent
from configs import get_settings
from langgraph.checkpoint.postgres import PostgresSaver
from agents.app_runtime import AppRuntime


def create_app_runtime()->AppRuntime:
    settings=get_settings()

    checkpointer_cm=PostgresSaver.from_conn_string(settings.database_url)
    checkpointer=checkpointer_cm.__enter__()

    checkpointer.setup()
    agent=build_agent(checkpointer)

    return AppRuntime(
        setting=settings,
        checkpointer=checkpointer,
        agent=agent
    )


def extract_assistant_reply(messages: list[BaseMessage])->str:
    """
    extract the assistant reply from the last state of the graph
    """

    for message in reversed(messages):
        if not isinstance(message, AIMessage):
            continue

        text=_content(message).strip()
        if text:
            return text
    return ""


def _content(message: BaseMessage)->str:
    """
    extract the content from the message
    """

    content=message.content
    if isinstance(content, str):
        return content
    
    if isinstance(content, list):
        parts: list[str]=[]
        for block in content:
            if isinstance(block, dict) and block.get("type")=="text":
                parts.append(str(block.get("text", "")))
            elif isinstance(block, str):
                parts.append(block)
        return "\n".join(parts)
    return str(content)