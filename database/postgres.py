import psycopg2
from db.db_interface import DatabaseInterface
from utils.config_loader import ConfigLoader

class PostgresDB(DatabaseInterface):
    def __init__(self):
        config = ConfigLoader.load_config()["database"]["postgres"]
        self.conn = psycopg2.connect(**config)
        self.cursor = self.conn.cursor()

    def insert_qso(self, qso):
        self.cursor.execute("""
            INSERT INTO qsos (callsign, qso_date, band, freq, mode, comment)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (qso["callsign"], qso["qso_date"], qso["band"], qso["freq"], qso["mode"], qso["comment"]))

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
