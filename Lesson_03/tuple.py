
masala_chai = ("cinnamon", "blackpepper", "honey")

(ingredient1, ingredient2, ingredient3) = masala_chai

ginger_ratio, cardimon_ratio = 2,1
print(ginger_ratio, cardimon_ratio)
ginger_ratio, cardimon_ratio = cardimon_ratio, ginger_ratio
print(ginger_ratio, cardimon_ratio)

# print(masala_chai)
# print(f"Ingredient1 {ingredient1}")

print(f"Is Cinnamon in masala Tea is {"cinnamon" in masala_chai}")

#  tuple is immutable
#  and list is mutable

# Liste

chai_essentials = ["tea leaves", "water", "sugar"]
chai_essentials.append("milk")

chai_upgradables = ["elichi", "black pepper", "ginger", "honey", "chai masala", "whip cream"]

chai_essentials.extend(chai_upgradables)
chai_essentials.insert(2, "biscuut")
print(chai_essentials)
last = chai_essentials.pop()
print(last)
print(chai_essentials)
chai_essentials.sort(reverse=True)
print(chai_essentials)