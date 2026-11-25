from repositories import UserRepository, ThreadRepository
from psycopg_pool import ConnectionPool


class UserService:

    def __init__(self, pool: ConnectionPool):
        self.pool=pool
        self.user_repository=UserRepository(self.pool)
        self.thread_repository=ThreadRepository(self.pool)


    def login_user(self, user_id: str, display_name: str | None=None)->dict:
        """
        Logins a user into the system.
        Creates the user if it doesn't exists.
        Creates a main thread for the user if doesn't exists.
        
        Args:
            user_id: The ID of the user.
            display_name: The display name of the user.
        Returns:
            dict: The user object.
        """

        # Create user if it doesn't exists
        user=self.user_repository.create_user(user_id=user_id, display_name=display_name)

        # Create a default thread_id for user
        default_thread_id=f"{user["user_id"]}:main"
        self.thread_repository.create_thread(user_id=user_id, thread_id=default_thread_id, title="Main Thread")

        return user

