from fastapi import FastAPI, APIRouter

from pythondi import Provider, configure, inject
import abc

router = APIRouter()


class Repo:
    """Interface class"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self):
        pass


class SQLRepo(Repo):
    """Impl class"""
    def __init__(self):
        pass

    def get(self):
        print('SQLRepo')


@router.route('/')
def home():
    usecase = Usecase()
    usecase.repo.get()
    return {'hello': 'world'}


class Usecase:
    @inject()
    def __init__(self, repo: Repo):
        self.repo = repo


def create_app():
    provider = Provider()
    provider.bind(Repo, SQLRepo)
    configure(provider=provider)
    app = FastAPI()
    app.include_router(router)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)