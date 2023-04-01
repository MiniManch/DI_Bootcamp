import string
import random
from faker import Faker

fake = Faker()


def get_random_string(length):
    letters = string.printable
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def populate_database(database, database_model):
    for i in range(10):
        full_fake_user = fake.profile()
        fake_user = {'id': i + 1,
                     'name': full_fake_user['name'].split(' ')[0],
                     'email': full_fake_user['mail'],
                     'address': full_fake_user['address']}
        fake_user = database_model(fake_user)
        database.session.add(fake_user)
    database.session.commit()


def redo_db(models, database):
    for model in models:
        for person in model.query.all():
            database.session.delete(person)

    database.session.commit()
    database.drop_all()
    database.create_all()


def populate_number_database(database, model):
    for i in range(15):
        fake_user = {'id': i+1,
                      'number': int(fake.msisdn()[2:9]),
                      'owner' : random.randint(1, 10)
                      }
        # fake_user = model(id=fake_user['id'], number=fake_user['number'], owner=fake_user['owner'])
        fake_user = model(fake_user)
        database.session.add(fake_user)
    database.session.commit()

