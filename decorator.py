def magic_box(func):
    def wrapper():
        print("Beep boop")
        func()
    return wrapper

@magic_box # dcecorator function, runs magic_box
def say_hello():
    print("Hello!")

say_hello()