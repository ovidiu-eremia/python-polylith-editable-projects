import pytest
from my_namespace.my_component import my_comp_func

@pytest.fixture
def setup():
    return my_comp_func
