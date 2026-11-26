from configs import get_settings
from repositories import ThreadRepository
from psycopg_pool import ConnectionPool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI


# Creating a In-Memory Short Term Memory
_MEM: dict[tuple[str, str], list]={}


class ChatService:

    def __init__(self, pool: ConnectionPool):
        self.pool=pool
        self.thread_repository=ThreadRepository(self.pool)
        self.settings=get_settings()
    

    def chat_once(self, user_id: str, thread_id: str, message: str)->tuple[str, str]:
        self.thread_repository.thread_belongs_to_a_user(thread_id, user_id)

        key=(user_id, thread_id)

        history=_MEM.setdefault(
            key,
            [SystemMessage(content="You are ChatUpAI, a helpful assistant")],
        )

        history.append(HumanMessage(content=message))
        model=ChatOpenAI(
            model=self.settings.chat_model,
            base_url=self.settings.llm_base_url,
            api_key=self.settings.llm_api_key
        )

        reply=model.invoke(history).content
        history.append(AIMessage(content=str(reply)))

        return (str(reply), thread_id)