import pytest


@pytest.fixture(scope='session')
def common_data():
    return ['data_1', 'data_2', 'data_3']
