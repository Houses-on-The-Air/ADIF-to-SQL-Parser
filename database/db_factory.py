from utils.config_loader import ConfigLoader
from db.mariadb import MariaDB
from db.oracle import OracleDB
from db.postgres import PostgresDB
from db.mssql import MSSQLDB

class DatabaseFactory:
    """Factory for creating database instances based on config."""

    @staticmethod
    def get_database():
        db_type = ConfigLoader.load_config()["database"]["type"]

        if db_type == "mariadb":
            return MariaDB()
        elif db_type == "postgres":
            return PostgresDB()
        elif db_type == "oracle":
            return OracleDB()
        elif db_type == "mssql":
            return MSSQLDB()
        else:
            raise ValueError(f"Unsupported database type: {db_type}")
