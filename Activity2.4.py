"""activity2.4 source code"""

import re

TEXT = "The rain in Spain"


def main() -> None:
    # Anchored search (equivalent to fullmatch on pattern without ^$)
    match = re.search(r"^The.*Spain$", TEXT)
    print(match)

    print(re.findall(r"ai", TEXT))
    print(re.findall(r"Portugal", TEXT))

    ws = re.search(r"\s", TEXT)
    if ws:
        print(
            f"The first white-space character is located in position: {ws.start()}")

    print(re.search(r"Portugal", TEXT))

    print(re.split(r"\s", TEXT))
    print(re.split(r"\s", TEXT, maxsplit=1))

    print(re.sub(r"\s", "9", TEXT))
    print(re.sub(r"\s", "9", TEXT, count=2))

    m = re.search(r"ai", TEXT)
    print(m)  # this will print a Match object (or None)

    m = re.search(r"\bS\w+", TEXT)
    if m:
        print(m.span())
        print(m.string)
        print(m.group())


if __name__ == "__main__":
    main()
