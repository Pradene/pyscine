import sys


def whatis(num: int):
    if num % 2 == 0:
        print("I'm Even")
    else:
        print("i'm Odd")


def main():
    try:
        if len(sys.argv) == 1:
            return

        if len(sys.argv) >= 3:
            raise AssertionError("more than one argument")

        try:
            num = int(sys.argv[1])
            whatis(num)
        except ValueError:
            raise AssertionError("argument is not an integer")

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
