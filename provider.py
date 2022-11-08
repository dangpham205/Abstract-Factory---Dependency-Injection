from pythondi import Provider, configure

from department_contract import DepartmentContract
from department_repository import DepartmentRepository


def init_di():
    provider = Provider()
    provider.bind(DepartmentContract, DepartmentRepository)
    configure(provider=provider)
