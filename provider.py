from pythondi import Provider, configure

from repos import DepartmentContract
from repos import DepartmentRepository


def init_di():
    provider = Provider()
    provider.bind(DepartmentContract, DepartmentRepository)
    configure(provider=provider)
