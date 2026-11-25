from psycopg_pool import ConnectionPool

class UserRepository:

    def __init__(self, pool: ConnectionPool):
        self.pool=pool


    def create_user(self, user_id: str, display_name: str | None=None)->dict:
        """
        Create a new user in the database.
        If a user with the given user_id already exists, return None.
        """

        user_id=user_id.strip()
        if not user_id:
            raise ValueError("User ID cannot be empty.")

        with self.pool.connection() as conn:
            conn.execute(
                """
                INSERT INTO chatup_users (user_id, display_name)
                VALUES (%s, %s)
                ON CONFLICT (user_id) DO NOTHING
                """,
                (user_id, display_name or user_id)
            )

            row=conn.execute(
                """
                SELECT user_id, display_name, created_at
                FROM chatup_users
                WHERE user_id=%s
                """,
                (user_id)
            ).fetchone()

        return row
