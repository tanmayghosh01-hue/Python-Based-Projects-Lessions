x = 10
def change_x(): 
    global  x
    x = 20

change_x()
print(x)

"""multiple returns"""
def calc(a, b):
    return a+b, a-b

sum, diff = calc(5,3)
print(sum, diff);
print(f"sum id : {id(sum)}")
diff = 1
print(f"diff id: {id(diff)}")

"""
 Mutable - That is changed
 Immutable - That is not changeable

 / divides the shit
 // divides and removes the after decimal shit

 truthy and falsy values

 splice

 string[start:stop:step]

"""

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor

print(f"Scaled flavour strenght {powerful_flavour}")

animal = 1_000_000_000
print(animal)
