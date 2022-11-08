from repos.department_contract import DepartmentContract
from sqlalchemy_abstract import SqlAchemyAbstract
from classes.department import Department

class DepartmentRepository(SqlAchemyAbstract, DepartmentContract):
    def __init__(self):
        self.set_model(Department)
        pass

    def get_by(self, user_id):
        return user_id
