import os

from models.databases import DATABASE_NAME, create_db, User, HistoryClient, ContactList, Session


if __name__ == '__main__':

    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        create_db()

    session = Session()
    user = User('Max', 'Gubanov', '12345678')

    session.add(user)
    session.commit()
    session.close()