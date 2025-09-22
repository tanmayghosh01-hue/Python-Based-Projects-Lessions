def cups() :
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"


chai = cups() 

for item in cups():
    print(item)
