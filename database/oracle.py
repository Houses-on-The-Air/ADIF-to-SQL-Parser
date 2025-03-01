import cx_Oracle
from database.db_interface import DatabaseInterface
from utils.config_loader import ConfigLoader

class OracleDB(DatabaseInterface):
    """
    OracleDB implementation of the DatabaseInterface.

    Methods
    -------
    __init__():
        Initializes the OracleDB connection using configuration settings.

    insert_qso(qso):
        Inserts a QSO record into the database.

    close():
        Commits the transaction and closes the database connection.
    """
    def __init__(self):
        """
        Initializes a new instance of the Oracle database connection.

        This method loads the Oracle database configuration, creates a DSN (Data Source Name),
        establishes a connection to the Oracle database using the provided credentials, and
        initializes a cursor for executing SQL queries.

        Attributes:
            conn (cx_Oracle.Connection): The connection object to the Oracle database.
            cursor (cx_Oracle.Cursor): The cursor object for executing SQL queries.

        Raises:
            KeyError: If any of the required configuration keys are missing.
            cx_Oracle.DatabaseError: If there is an error connecting to the Oracle database.
        """
        config = ConfigLoader.load_config()["database"]["oracle"]
        dsn = cx_Oracle.makedsn(config["host"], config["port"], service_name=config["service_name"])
        self.conn = cx_Oracle.connect(user=config["user"], password=config["password"], dsn=dsn)
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
            VALUES (:1, :2, :3, :4, :5, :6)
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
