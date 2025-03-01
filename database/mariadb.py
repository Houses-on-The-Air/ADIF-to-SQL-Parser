import pymysql
from database.db_interface import DatabaseInterface
from utils.config_loader import ConfigLoader

class MariaDB(DatabaseInterface):
    def __init__(self):
        """
        Initializes a new instance of the database connection.

        This method loads the MariaDB configuration using the ConfigLoader,
        establishes a connection to the MariaDB database, and creates a cursor
        for executing SQL queries.

        Attributes:
            conn (pymysql.connections.Connection): The connection object to the MariaDB database.
            cursor (pymysql.cursors.Cursor): The cursor object for executing SQL queries.
        """
        config = ConfigLoader.load_config()["database"]["mariadb"]
        self.conn = pymysql.connect(**config)
        self.cursor = self.conn.cursor()

    def insert_qso(self, qso):
        """
        Inserts a QSO (contact) record into the qsos table in the database.

        Args:
            qso (dict): A dictionary containing the QSO details with the following keys:
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

        This method commits any pending transactions to the database,
        closes the cursor, and then closes the connection to the database.
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
