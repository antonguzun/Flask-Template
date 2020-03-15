import os

import pytest

from myapp.app import create_app


@pytest.fixture(scope="function")
def app():
    assert os.getenv("ENV") == "TEST", "You must run tests in TEST environment only"
    app = create_app()
    return app


@pytest.fixture(scope="function", autouse=True)
def db(app, request):
    """
    Returns session-wide initialised database.
    """
    from myapp.models import Base
    from database import engine

    assert engine.url.database.split("_")[0] == "test"

    Base.metadata.create_all(engine)
    yield
    from database import db_session

    db_session.remove()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function", autouse=True)
def assert_session():
    from database import db_session

    assert db_session.bind.engine.url.database.split("_")[0] == "test", "You must use test database"


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
