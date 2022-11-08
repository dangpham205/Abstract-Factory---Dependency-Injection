from abc import ABCMeta, abstractmethod
from sqlalchemy_contract import SqlAchemyContracts
class DepartmentContract(SqlAchemyContracts):
    __metaclass__ = ABCMeta
    @abstractmethod
    def get_by(self, user_id):
        pass
