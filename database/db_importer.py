from db.postgres import PostgresDatabase  # Change this based on config

class DataImporter:
    """Handles importing parsed QSO data into the selected database."""

    def __init__(self, db_instance):
        self.db = db_instance

    def import_data(self, qsos):
        for qso in qsos:
            self.db.insert_qso(qso)
        self.db.close()
