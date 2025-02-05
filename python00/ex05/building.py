import sys


def building(s: str):
    lower = 0
    upper = 0
    digit = 0
    space = 0
    punct = 0

    for c in s:
        if c.islower():
            lower += 1
        elif c.isupper():
            upper += 1
        elif c.isdigit():
            digit += 1
        elif c.isspace():
            space += 1
        else:
            punct += 1

    print(
        f"The text contains {len(s)} characters:\n"
        f"{upper} upper letters\n"
        f"{lower} lower letters\n"
        f"{punct} punctuation marks\n"
        f"{space} spaces\n"
        f"{digit} digits"
    )


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("too many arguments")

        if len(sys.argv) != 2:
            try:
                print("What is the text to count?")
                text = sys.stdin.readline()
            except EOFError:
                pass
            except KeyboardInterrupt:
                exit(1)
        else:
            text = sys.argv[1]

        building(text)

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
