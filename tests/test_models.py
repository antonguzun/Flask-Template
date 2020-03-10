from myapp.models import User


def test_db():
    from myapp.app import db

    assert db.engine.url.database.split("_")[0] == "test"

    assert User.query.all() == []
    user = User.create(username="tester", email="tester@gmail.com")
    assert User.get_by_id(user.id) == user
    user.username = "tester_fixed"
    user.save()
    assert User.get_by_id(user.id).username == "tester_fixed"
    user.delete(user.id)
    assert User.query.all() == []
