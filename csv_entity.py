from abc import ABCMeta, abstractmethod, abstractstaticmethod

class CSVEntity(metaclass=ABCMeta):
    @abstractmethod
    def to_csv(self):
        return None

    @abstractstaticmethod
    def dict_from_csv(csv):
        return {}
