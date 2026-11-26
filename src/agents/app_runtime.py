from langchain_core.runnables import RunnableConfig
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.postgres import PostgresSaver
from configs import Settings
from langgraph.graph.state import CompiledStateGraph
from dataclasses import dataclass

@dataclass
class AppRuntime:

    setting: Settings
    checkpointer: PostgresSaver
    agent: CompiledStateGraph

    def chat(self, user_id: str, thread_id: str, user_message: str)->tuple[str, list[BaseMessage]]:
        config=self._chat_config(user_id, thread_id)
        self.agent.invoke(
            {"messages": [{"role": "user", "content": user_message}]},
            config=config
        )

        # Get current state of graph i.e. data being processed (messages, results etc)
        snapshot=self.agent.get_state(config)

        message=(snapshot.values or {}).get("messages") or []
        

    
    def _chat_config(self, user_id: str, thread_id: str)->RunnableConfig:
        return {
            "configurable": {
                "thread_id": thread_id,
                "user_id": user_id,
                "langgraph_user_id": user_id
            }
        }