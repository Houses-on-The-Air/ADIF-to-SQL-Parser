from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    """Abstract class for all database connections."""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert_qso(self, qso):
        pass

    @abstractmethod
    def close(self):
        pass
