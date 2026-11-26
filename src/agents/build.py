from configs import get_settings
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.graph.state import CompiledStateGraph
from langchain.agents import create_agent


def build_agent(checkpointer: PostgresSaver)->CompiledStateGraph:
    settings=get_settings()

    return create_agent(
        model=settings.chat_model,
        tools=[],
        checkpointer=checkpointer,
    ).with_config({
        "recursion_limit": 50
    })