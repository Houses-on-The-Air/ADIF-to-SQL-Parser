from postgres import PostgresDB  # Change this based on config

class DataImporter:
    """
    DataImporter is responsible for importing parsed QSO data into the selected database.

    Attributes:
        db (Database): An instance of the database where QSOs will be imported.

    Methods:
        import_data(qsos):
            Imports a list of QSO data into the database and closes the database connection.

            Args:
                qsos (list): A list of QSO data to be imported.
    """
    def __init__(self, db_instance):
        """
        Initializes the db_importer with a database instance.

        Args:
            db_instance: An instance of the database to be used by the importer.
        """
        self.db = db_instance

    def import_data(self, qsos):
        """
        Imports a list of QSOs (contacts) into the database.

        Args:
            qsos (list): A list of QSO objects to be inserted into the database.

        Returns:
            None
        """
        for qso in qsos:
            self.db.insert_qso(qso)
        self.db.close()
