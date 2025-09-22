def chai_requests(*fixed, **specified) :
    print(fixed)
    print(specified)


chai_requests("mixed green", 1, 2 , True, sweetener="honey",foam="yes")

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai)