import pytest

class FakeResponse:

    def __init__(self, status=200, body=""):
        self.status = status
        self.body = body


@pytest.fixture
def response():
    def apply(status=200, body=""):
        return FakeResponse(status=status, body=body)
    return apply