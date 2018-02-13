from models import User, Session


def test_models(db_session):
    user = db_session.query(User).first()
    assert user is None

    new_user = User(
        name="user",
        surname="userovich",
        password="strong-password"
    )
    db_session.add(new_user)

    loaded_user = db_session.query(User).first()
    assert new_user == loaded_user

    session = db_session.query(Session).first()
    assert session is None

    new_session = Session(user=user)
    db_session.add(new_session)

    loaded_session = db_session.query(Session).first()
    assert new_session == loaded_session
    assert loaded_user.user == new_user
