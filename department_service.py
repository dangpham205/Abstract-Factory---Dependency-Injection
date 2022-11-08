from pythondi import inject
from department_contract import DepartmentContract
class DepartmentService:
    @inject()
    def __init__(self, dep_repo: DepartmentContract):
        self.dep_repo = dep_repo
