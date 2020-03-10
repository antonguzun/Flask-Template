class TestUserListView:
    def test_success(self, client):
        assert client.get("/users/").status_code == 200
