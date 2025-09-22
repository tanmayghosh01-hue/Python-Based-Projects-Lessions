# here we see how we can use zip

students = ["Tanmay", "Arun", "Julia", "Priya"]
score = [33, 23, 66, 22]
combined_list = []

for name, score in zip(students, score):
    combined_list.append(f"{name} : {score}")


print(combined_list)
print(type(students))