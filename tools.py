from faker import Faker


class RegData:
    @staticmethod
    def create_user():
        fake = Faker()
        data = {
            'email': fake.free_email(),
            'password': fake.password(length=12),
            'name': fake.name()
        }
        return data

    reg_without_email = {
        'email': '',
        'password': 'test12313',
        'name': 'tests'
    }

    reg_without_pswd = {
        'email': 'test123131@ya.ru',
        'password': '',
        'name': 'tests'
    }

    reg_without_name = {
        'email': 'test123131@ya.ru',
        'password': 'test12313',
        'name': ''
    }

    correct_user = {
        'email': 'test12313@ya.ru',
        'password': 'test12313'
    }

    reg_double_user = {
        'name': 'tst',
        'email': 'test12313@ya.ru',
        'password': 'test12313'
    }

    incorrect_user = {
        'email': 'test1231@ya.ru',
        'password': 'test12313'
    }
