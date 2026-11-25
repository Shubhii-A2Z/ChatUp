from repositories import ThreadRepository
from psycopg_pool import ConnectionPool


class ThreadService:

    def __init__(self, pool: ConnectionPool):
        self.pool=pool
        self.thread_repository=ThreadRepository(self.pool)


    def get_threads_for_user(self, user_id: str)->list[dict]:
        """
        Get all threads for a user.

        Args:
            user_id (str): The ID of the user.
        
        Returns:
            list[dict]: List of threads for the user.
        """
        return self.thread_repository.list_threads(user_id=user_id)

