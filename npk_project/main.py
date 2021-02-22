import os


def main():
    os.system("flake8 > /results/flake8_results.txt")
    tests_path = filter(lambda x: 'test' in x, os.listdir(path="./tests"))
    tests_names = map(lambda x: x.split('.')[0], tests_path)
    for test in tests_names:
        mod = __import__('tests.' + test)
        test_class = getattr(mod, test).SomeTest
        test_class(test).start_check()


if __name__ == '__main__':
    main()
