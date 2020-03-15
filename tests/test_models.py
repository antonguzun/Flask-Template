from database import db_session
from myapp.models import User


class TestDatabase:
    def test_db(self):
        assert User.query.all() == []

        user = User(username="tester", email="tester@gmail.com")
        db_session.add(user)
        db_session.commit()
        assert db_session.query(User).get(user.id) == user

        user.username = "tester_fixed"
        db_session.commit()

        assert db_session.query(User).get(user.id).username == "tester_fixed"
        db_session.delete(user)
        db_session.commit()
        assert User.query.all() == []
