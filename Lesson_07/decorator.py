from functools import wraps
def my_decorator(func):
  @wraps(func)
  def wrapper():
    print("Before function runs")
    func()
    print("After function runs")
  return wrapper


@my_decorator
def chai() :
  print("Hello your matcha is ready")


chai()
print(chai.__name__)