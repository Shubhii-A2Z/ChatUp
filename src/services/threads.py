import uuid
from repositories import ThreadRepository, UserRepository
from psycopg_pool import ConnectionPool


class ThreadService:

    def __init__(self, pool: ConnectionPool):
        self.pool=pool
        self.thread_repository=ThreadRepository(self.pool)
        self.user_repository=UserRepository(self.pool)


    def get_threads_for_user(self, user_id: str)->list[dict]:
        """
        Get all threads for a user.

        Args:
            user_id (str): The ID of the user.
        
        Returns:
            list[dict]: List of threads for the user.
        """
        return self.thread_repository.list_threads(user_id=user_id)


    def create_new_thread(self, user_id: str, title: str | None=None)->dict:
        # First ensuring if user exists
        self.user_repository.create_user(user_id=user_id)

        # Create a default new thread_id for user
        thread_id=f"{user_id}:{uuid.uuid4().hex[:8]}"

        return self.thread_repository.create_thread(user_id=user_id, thread_id=thread_id, title=title)
