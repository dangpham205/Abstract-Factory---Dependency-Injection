from abc import ABCMeta, abstractmethod
from sqlalchemy_contract import SqlAchemyContracts



class SqlAchemyAbstract(SqlAchemyContracts):
    __metaclass__ = ABCMeta
    _model = None

    # def __init__(self, model,
    #             activity_log: ActivityLog = Depends(ActivityLog)):
    #     self.service = activity_log
    #     pass

    @abstractmethod
    def get_model(self):
        return self._model

    @abstractmethod
    def set_model(self, model):
        self._model = model

    @abstractmethod
    def get_all(self, with_trash: bool = False):
        # query = db.query(self._model).all()
        # if not with_trash:
        # query = query.filter(self._model.deleted_at.is_(None))
        # return query.get()
        return self._model.data
