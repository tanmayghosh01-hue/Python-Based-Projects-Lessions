flavour = ["masala", "ginger", "lemon", "mint"]

print(f"Available flavours {flavour}")

while (flavour_user := input("Choose your flavour ")) not in flavour :
    print(f"sorry {flavour_user} is not available")

print(f"you choose {flavour_user} chai")