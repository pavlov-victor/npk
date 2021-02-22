import faker
from tools import TestClass

faker = faker.Faker()


class SomeTest(TestClass):

    def right_version(self, data):
        return data[0] + data[1]

    def generate_data(self):
        return [faker.random_int(), faker.random_int()]
