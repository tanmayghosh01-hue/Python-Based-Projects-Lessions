def local_chai():
  yield "Masala Chai"
  yield "Ginger Chai"


def foreign_chai():
  yield "oolong chai"
  yield "matcha chai"


def full_menu():
  yield from local_chai()
  yield from foreign_chai()
  
  
for chai in full_menu():
  print(chai)
  
def chai_stall():
  try:
    while True:
      order = yield "Waiting for chai order"
  except:
    print("Stall closed, No more chai")
    
stall = chai_stall()
print(next(stall))
print(stall.send("Masala Chai"))
stall.close()