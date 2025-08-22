age = 19
is_student = False
name = "Tanmay"

print(id(name))

# if age > 18 and is_student:
#     print("Adult Student")
# else:
#     print("Stranger")

# Falsy → 0, "" (empty string), [], {}, None, False

if not is_student:
    print("not a student")

if (age > 18 and is_student) or (name == "Tanmay"):
    print("Allowed")