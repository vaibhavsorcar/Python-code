def greet(fx):
    def mfx(*args,**kwargs):
        print("Beginning of a function....")
        fx(*args,**kwargs)
        print('Thank you for using the functions. \n')
    return mfx

@greet
def hello():
    print('hello world')
hello()

@greet
def add(a, b):
    print(a+b)
add(1,2)
