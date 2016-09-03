from abc import ABCMeta, abstractmethod

class CSVEntity(metaclass=ABCMeta):
    @abstractmethod
    def to_csv(self):
        return None
