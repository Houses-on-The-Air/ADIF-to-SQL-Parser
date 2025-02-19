from utils.config_loader import load_config
from database.mariadb import MariaDB
from database.postgres import PostgresDB
from database.oracle import OracleDB
from database.mssql import MSSQLDB

def get_database():
    """Factory method to get the correct database implementation."""
    config = load_config()
    db_type = config["database"]["type"]

    databases = {
        "mariadb": MariaDB,
        "postgres": PostgresDB,
        "oracle": OracleDB,
        "mssql": MSSQLDB
    }

    if db_type not in databases:
        raise ValueError(f"Unsupported database type: {db_type}")

    return databases[db_type](config["database"][db_type])
