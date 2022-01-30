import os


class Config:
    def __init__(self):
        self.sql_host = os.getenv("SQL_HOST", "localhost")
        self.sql_username = os.getenv("SQL_USERNAME", "root")
        self.sql_password = os.getenv("SQL_PASSWORD", "toor")
        self.sql_database_name = os.getenv("SQL_DATABASE_NAME", "todo")
        self.sql_port = os.getenv("SQL_PORT", 5432)
        self.sql_schema = os.getenv("SQL_SCHEMA", "public")
