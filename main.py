from abc import ABC, abstractmethod
from department_service import DepartmentService
from provider import init_di


class AbstractClass(ABC):
    @abstractmethod
    def func(self):
        pass
    
    def a(self):
        return 'a'

class ChildClass(AbstractClass):
    def func(self):
        out = "This is an output"
        return out
    
    def t(self):
        return 't'

if __name__ == '__main__':
    obj = ChildClass()
    print(obj.func())
    print(obj.a())
    print(obj.t())
    
    init_di()
    service = DepartmentService()
    data = service.dep_repo.get_all()
    print(data)
    data = service.dep_repo.get_model()
    print(data)
    # try:
    #     service = DepartmentService()
    #     data = service.dep_repo.get_all()
    #     print(data)
    # except Exception as e:
    #     print(e)