from models import User


def test_models(db_session):
    user = db_session.query(User).first()
    assert user is None

    new_user = User(name="user", password="strong-password")
    db_session.add(new_user)

    loaded_user = db_session.query(User).first()
    assert new_user == loaded_user


