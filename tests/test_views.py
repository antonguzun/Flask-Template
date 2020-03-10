import pytest


class TestUserListView:
    def test_success(self, client):
        assert client.get('/').status_code == 200
