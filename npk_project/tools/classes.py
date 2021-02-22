import os
import time


class TestClass(object):
    """
    Класс для создания тестов, требуется переопределить
    2 метода - right_version как правильный вариант
    и generate_data для создания данных
    """

    def right_version(self, data):
        """Правильный вариант решения для сравнения."""

        raise AttributeError(
            'Not overrided right_version method'
        )

    def generate_data(self):
        """Возвращает список входных данных в функцию."""

        raise AttributeError(
            'Not overrided generate_data method'
        )

    def __init__(self, test_name):
        self.test_name = test_name

    def get_target_tests(self):
        test_name = '_'.join(self.test_name.split('_')[:2])
        tests_path = filter(lambda x: test_name in x,
                            os.listdir(path="reviews"))
        tests_names = map(lambda x: x.split('.')[0], tests_path)
        self.tests_names = list(tests_names)

    def save_results(self, result, name, tracks=[]):
        with open('/results/' + name + '_result.txt', 'w+') as f:
            f.write(f'{name}: result - {result}\n')
            for track in tracks:
                f.write(f'{name}: {track}')

    def check(self, test_name, data):
        mod = __import__('reviews.' + test_name)
        result = getattr(mod, test_name).result
        return result(*data)

    def get_track_options(self):
        """Параметры отслеживания."""

        return ['time']

    def start_check(self):
        data = self.generate_data()
        self.get_target_tests()
        for test_name in self.tests_names:
            try:
                if self.check(test_name, data) == self.right_version(data):
                    tracks = []
                    if 'time' in self.get_track_options():
                        start = time.time()
                        self.check(test_name, data)
                        tracks.append(f'time - {time.time() - start}')
                    self.save_results(
                        'success',
                        test_name,
                        tracks
                    )
                else:
                    self.save_results('test not right', test_name)
            except Exception as e:
                self.save_results(f'failed', test_name, tracks=[f'error - {e}'])
