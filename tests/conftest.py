from shutil import copy

import pytest
from ..recipes_api.api import create_app
from ..recipes_api.constants import PROJECT_ROOT, DATAFILE

@pytest.fixture
def client(tmpdir):
    copy(DATAFILE, tmpdir.dirpath())
    
    temp_datafile = f"{tmpdir.dirpath()}\{DATAFILE}"
    
    app = create_app(temp_datafile)
    app.config["TESTING"] = True
    
    with app.test_client() as client:
        yield client