import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. "
}


def convert_morse(s):
    morse = ""
    for c in s.upper():
        if c in NESTED_MORSE:
            morse += NESTED_MORSE[c]
        else:
            raise AssertionError("bad arguments")

    return morse.strip()


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("wrong number of arguments")

        print(convert_morse(sys.argv[1]))

    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
