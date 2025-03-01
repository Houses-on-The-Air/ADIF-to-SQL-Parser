from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    """
    Abstract class for all database connections.

    Methods:
        connect():
            Establishes a connection to the database.

        insert_qso(qso):
            Inserts a QSO (contact) record into the database.

        close():
            Closes the connection to the database.
    """
    @abstractmethod
    def connect(self):
        """
        Establishes a connection to the database.

        This method should be implemented to create a connection to the database
        using the appropriate database driver and connection parameters.

        Raises:
            DatabaseConnectionError: If the connection to the database fails.
        """
        pass

    @abstractmethod
    def insert_qso(self, qso):
        """
        Inserts a QSO (contact) record into the database.

        Args:
            qso (dict): A dictionary containing QSO data. The keys should correspond
                        to the database column names and the values should be the data
                        to be inserted.

        Returns:
            None
        """
        pass

    @abstractmethod
    def close(self):
        """
        Closes the database connection.

        This method should be called to properly close the connection to the database
        and release any resources held. It is important to call this method to avoid
        potential memory leaks or other issues related to open connections.
        """
        pass
