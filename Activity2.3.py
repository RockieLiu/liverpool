#Activity 2.3  source code



def main() -> None:
    greek_island = "Santorini"
    print(greek_island)

    earth_age_bln = 4.4
    universe_age_bln = 14  # TODO: use or remove
    earth_age_bln += 0.1
    print(earth_age_bln)

    asia_wishlist = [
        "Bhutan",
        "Ha Long",
        "Laos",
        "Danxia",
        "Seoul",
        "Khao Sok",
        "Cebu",
        "Chiang Mai",
        "Ho Chi Minh",
    ]
    print(asia_wishlist)

    msg = "life is beautiful"
    if msg == "I love you":
        print("propose")
    else:
        print("wait xP")

    net_earnings = 10_000_000
    if net_earnings >= 100_000_000:
        print("Large Cap")
    else:
        print("Small Cap")

    lst = ["soccer", "swimming", "running", "skiing"]
    if "rock climbing" not in lst:
        print("boo")

    web_data = "techresearch and computervision"
    if "@" in web_data:
        print("e-mail address")
    elif any(ch.isdigit() for ch in web_data):
        print("phone number")
    else:
        print("not e-mail nor phone number")

    a = 10 + 20
    b = 100 - 1
    c = 50 / 7
    d = 50 // 7
    e = 10 % 8
    f = 5 ** 2
    print(a, b, c, d, e, f, sep="\n ")


if __name__ == "__main__":
    main()
