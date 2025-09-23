def decorator(func):
    def wrapper():
        print("*******")
        func()
        print("*******")
    return wrapper

@decorator
def hello():
    print("hello")

hello()