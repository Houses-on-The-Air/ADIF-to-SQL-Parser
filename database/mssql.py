import pyodbc
from database.db_interface import DatabaseInterface
from utils.config_loader import ConfigLoader

class MSSQLDB(DatabaseInterface):
    """
    A class to interact with an MSSQL database.

    Methods
    -------
    __init__():
        Initializes the database connection using configuration settings.

    insert_qso(qso):
        Inserts a QSO record into the database.

    close():
        Commits the transaction and closes the database connection.
    """
    def __init__(self):
        """
        Initializes a new instance of the class, establishing a connection to the MSSQL database.

        The connection parameters are loaded from a configuration file using the ConfigLoader class.
        The connection string is constructed using the loaded parameters and used to establish a connection
        to the MSSQL database via pyodbc.

        Attributes:
            conn (pyodbc.Connection): The connection object to the MSSQL database.
            cursor (pyodbc.Cursor): The cursor object for executing SQL queries.
        """
        config = ConfigLoader.load_config()["database"]["mssql"]
        conn_str = f"DRIVER={{SQL Server}};SERVER={config['host']};DATABASE={config['database']};UID={config['user']};PWD={config['password']}"
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def insert_qso(self, qso):
        """
        Inserts a QSO (contact) record into the qsos table in the database.

        Args:
            qso (dict): A dictionary containing the QSO data with the following keys:
                - callsign (str): The callsign of the contact.
                - qso_date (str): The date of the QSO.
                - band (str): The band on which the QSO was made.
                - freq (str): The frequency of the QSO.
                - mode (str): The mode of the QSO.
                - comment (str): Any additional comments about the QSO.

        Returns:
            None
        """
        self.cursor.execute("""
            INSERT INTO qsos (callsign, qso_date, band, freq, mode, comment)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (qso["callsign"], qso["qso_date"], qso["band"], qso["freq"], qso["mode"], qso["comment"]))

    def close(self):
        """
        Closes the database connection.

        This method commits any pending transactions to the database, closes the cursor,
        and then closes the connection to the database.
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
