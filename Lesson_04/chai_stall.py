chai = input("give your chai size order smol/medium/large: ").lower()


if chai == "small":
    print("price is 10/- Rupees")
elif chai == "medium":
    print("price is 15/- Rupees")
elif chai == "large":
    print("price is 20/- Rupees")
else:
    print("Unknown cup size")