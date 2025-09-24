def infinite_chai():
  count = 1
  while True:
    yield f"Refill #{count}" # with next function the function will be pause here in yield
    count += 1
  
  
refill = infinite_chai()

for _ in range(6):
  print(next(refill))