from functools import wraps


def require_admin(func) :
  
  @wraps(func)
  def wrapper(user_role):
    if user_role != "admin":
      print(f"Access Denied {user_role} only admin nigga")
      return None
    else :
      return func(user_role)
    
  return wrapper



@require_admin
def greet(name):
  print(f"Welcome to garden {name} nigga")
  
greet("Tanmay")
greet("admin")
     
    