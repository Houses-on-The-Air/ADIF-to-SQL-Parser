import pyodbc
from db.db_interface import DatabaseInterface
from utils.config_loader import ConfigLoader

class MSSQLDB(DatabaseInterface):
    def __init__(self):
        config = ConfigLoader.load_config()["database"]["mssql"]
        conn_str = f"DRIVER={{SQL Server}};SERVER={config['host']};DATABASE={config['database']};UID={config['user']};PWD={config['password']}"
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def insert_qso(self, qso):
        self.cursor.execute("""
            INSERT INTO qsos (callsign, qso_date, band, freq, mode, comment)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (qso["callsign"], qso["qso_date"], qso["band"], qso["freq"], qso["mode"], qso["comment"]))

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
