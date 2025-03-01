from utils.config_loader import load_config
from database.mariadb import MariaDB
from database.postgres import PostgresDB
from database.oracle import OracleDB
from database.mssql import MSSQLDB

def get_database():
    """
    Factory method to get the correct database implementation.

    This method reads the database configuration from a configuration file,
    determines the type of database to use, and returns an instance of the
    appropriate database class.

    Returns:
        An instance of the database class corresponding to the configured
        database type.

    Raises:
        ValueError: If the configured database type is not supported.
    """
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
