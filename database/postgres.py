import psycopg2
from database.db_interface import DatabaseInterface
from utils.config_loader import ConfigLoader

class PostgresDB(DatabaseInterface):
    """
    A class to interact with a PostgreSQL database.

    Methods
    -------
    __init__():
        Initializes the database connection and cursor.
    insert_qso(qso):
        Inserts a QSO record into the database.
    close():
        Commits the transaction, closes the cursor, and closes the database connection.
    """
    def __init__(self):
        """
        Initializes a new instance of the database connection.

        This constructor loads the PostgreSQL database configuration using
        ConfigLoader and establishes a connection to the database. It also
        creates a cursor for executing database operations.

        Attributes:
            conn (psycopg2.extensions.connection): The connection object to the PostgreSQL database.
            cursor (psycopg2.extensions.cursor): The cursor object for executing database operations.
        """
        config = ConfigLoader.load_config()["database"]["postgres"]
        self.conn = psycopg2.connect(**config)
        self.cursor = self.conn.cursor()

    def insert_qso(self, qso):
        """
        Inserts a QSO (contact) record into the qsos table in the database.

        Parameters:
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
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (qso["callsign"], qso["qso_date"], qso["band"], qso["freq"], qso["mode"], qso["comment"]))

    def close(self):
        """
        Closes the database connection.

        This method commits any pending transactions to the database, closes the
        cursor, and then closes the connection to the database.
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
