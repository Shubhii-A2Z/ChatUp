from psycopg_pool import ConnectionPool


class ThreadRepository:

    def __init__(self, pool: ConnectionPool):
        self.pool=pool


    def list_threads(self, user_id: str)->list[dict]:
        """Return list of all threads for a user ordered by last modified."""

        with self.pool.connection() as conn:
            rows=conn.execute(
                """
                SELECT thread_id, title, created_at, updated_at
                FROM chatup_threads
                WHERE user_id = %s
                ORDER BY updated_at DESC
                """,
                (user_id,)
            ).fetchall()

        return list[rows]
    
    
    def create_thread(self, user_id: str, thread_id: str, title: str="New Thread")->dict:
        """Create a new thread for the given user."""

        with self.pool.connection() as conn:
            conn.execute(
                """
                INSERT INTO chatup_threads (thread_id, user_id, title)
                VALUES (%s, %s, %s)
                ON CONFLICT (thread_id) DO NOTHING
                """,
                (thread_id, user_id, title,)
            )

            row=conn.execute(
                """
                SELECT thread_id, title, created_at, updated_at
                FROM chatup_threads
                WHERE user_id=%s
                """,
                (user_id,)
            ).fetchone()
        
        return row


    def update_thread_title(self, user_id: str, thread_id: str, title: str)->dict | None:
        """Update the title of a thread"""

        with self.pool.connection() as conn:
            row=conn.execute(
                """
                UPDATE chatup_threads
                SET title=%s, updated_at=NOW()
                WHERE thread_id=%s AND user_id=%s
                RETURNING thread_id, title, created_at, updated_at
                """,
                (title, thread_id, user_id,)
            ).fetchone()

        return row


    def touch_thread(self, thread_id: str)->None:
        """Update the updated_at timestamp of thread whenever a new message is added."""

        with self.pool.connection() as conn:
            conn.execute(
                """
                UPDATE chatup_threads
                SET updated_at=NOW()
                WHERE thread_id=%s
                """,
                (thread_id,)
            )


    def thread_belongs_to_a_user(self, thread_id: str, user_id: str)->bool:
        """Return true if the thread belongs to a user."""

        with self.pool.connection() as conn:
            row=conn.execute(
                """
                SELECT 1
                FROM chatup_threads
                WHERE thread_id=%s AND user_id=%s
                """,
                (thread_id, user_id,)
            ).fetchone()

        return row is not None