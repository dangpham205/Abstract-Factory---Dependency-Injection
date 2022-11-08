from abc import ABCMeta, abstractmethod

class SqlAchemyContracts:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_model(self):
        pass
    
    @abstractmethod
    def set_model(self, model):
        pass
    
    @abstractmethod
    def get_all(self, with_trash: bool = False):
        pass

    
