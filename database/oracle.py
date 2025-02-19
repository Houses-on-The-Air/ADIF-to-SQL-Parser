import cx_Oracle
from db.db_interface import DatabaseInterface
from utils.config_loader import ConfigLoader

class OracleDB(DatabaseInterface):
    """OracleDB implementation of the DatabaseInterface."""

    def __init__(self):
        config = ConfigLoader.load_config()["database"]["oracle"]
        dsn = cx_Oracle.makedsn(config["host"], config["port"], service_name=config["service_name"])
        self.conn = cx_Oracle.connect(user=config["user"], password=config["password"], dsn=dsn)
        self.cursor = self.conn.cursor()

    def insert_qso(self, qso):
        self.cursor.execute("""
            INSERT INTO qsos (callsign, qso_date, band, freq, mode, comment)
            VALUES (:1, :2, :3, :4, :5, :6)
        """, (qso["callsign"], qso["qso_date"], qso["band"], qso["freq"], qso["mode"], qso["comment"]))

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
