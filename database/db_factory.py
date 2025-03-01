from database.mariadb import MariaDB
from database.mssql import MSSQLDB
from database.oracle import OracleDB
from database.postgres import PostgresDB
from utils.config_loader import ConfigLoader


class DatabaseFactory:
    """
    Factory class for creating database instances based on configuration.

    Methods
    -------
    get_database() -> Union[MariaDB, PostgresDB, OracleDB, MSSQLDB]
        Static method that returns an instance of a database class based on the
        database type specified in the configuration. Raises a ValueError if the
        database type is unsupported.

    Raises
    ------
    ValueError
        If the database type specified in the configuration is unsupported.

    Examples
    --------
    >>> db_instance = DatabaseFactory.get_database()
    >>> type(db_instance)
    <class 'MariaDB'>  # or PostgresDB, OracleDB, MSSQLDB based on config
    """
    @staticmethod
    def get_database():
        """
        Retrieve a database connection instance based on the configuration.

        This function reads the database type from the configuration and returns
        an instance of the corresponding database class. Supported database types
        are "mariadb", "postgres", "oracle", and "mssql".

        Returns:
            MariaDB: An instance of the MariaDB class if the database type is "mariadb".
            PostgresDB: An instance of the PostgresDB class if the database type is "postgres".
            OracleDB: An instance of the OracleDB class if the database type is "oracle".
            MSSQLDB: An instance of the MSSQLDB class if the database type is "mssql".

        Raises:
            ValueError: If the database type specified in the configuration is not supported.
        """
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
