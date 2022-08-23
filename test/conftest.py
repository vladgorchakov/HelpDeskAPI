from pytest import fixture


@fixture(scope='session')
def get_token():
    return 'token'
