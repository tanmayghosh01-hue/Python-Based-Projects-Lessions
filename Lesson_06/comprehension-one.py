menu = [
    "Masala chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai",
    "Green Tea",
    "Masala Tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]

# print(iced_tea)

# { experession for item in iterable if condition }

unique_chai = {chai for chai in menu if len(chai) < 10}
# print(unique_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black Pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients }

# print(unique_spices)

tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea : price / 100 for tea, price in tea_prices_inr.items()}

print(type(tea_prices_usd))

# for tea, prices in tea_prices_inr.items():
    # print(tea ,": ", prices)