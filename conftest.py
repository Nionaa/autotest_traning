from Precondition.application import Application
import pytest

@pytest.fixture(scope="session")
def app_fixture():
    app = Application()

    yield app
    app.destroy()
