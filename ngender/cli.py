import argparse

from .ngender import guess


def main():
    parser = argparse.ArgumentParser(
        description='Guess gender for Chinese names')

    parser.add_argument('names', nargs='+',
                        help='chinese names to guess')
    args = parser.parse_args()

    for name in args.names:
        gender, prob = guess(name)
        print('name: {} => gender: {}, probability: {}'
              ''.format(name, gender, prob))


if __name__ == '__main__':
    main()
