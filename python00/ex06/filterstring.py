import sys
from ft_filter import filter


def filterstring(s: str, num: int):
    return filter(lambda x: len(x) > num, s.split())


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError()

        try:
            num = int(sys.argv[2])
            print(filterstring(sys.argv[1], num))
        except ValueError:
            raise AssertionError()

    except AssertionError as e:
        print(f"{type(e).__name__}: bad arguments")


if __name__ == "__main__":
    main()
