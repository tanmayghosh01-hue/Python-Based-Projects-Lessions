

coffee_materials = {"bean": "blue Tokai bean", "water": "RO water", "milk" : "Amul"}

coffee_materials.popitem()

plus_materials = {"filter": "pressure_stainer"}

coffee_materials.update(plus_materials)


print(coffee_materials)

coffee_water = coffee_materials.get("water", "no water")

print(coffee_water)