def token_dispenser(start :int = 1):
  try: 
    token = start
    while True:
      new_value = yield token
      
      if new_value is not None:
        token = new_value
      else:
        token += 1
    
  except GeneratorExit:
    print("Dispenser closed")
    
    
dispenser = token_dispenser()
print(next(dispenser))
print(next(dispenser))
dispenser.close()