# User-defined functions
def greeting():
    print("Hello world")

greeting() #calling a function

def add():
    print(5*3)
add()

# parameters and arguments
def student(firstname, course, age):
    print(firstname, course, age)
student("Ian", "MIT", 20)

# built in library function
y = max(13, 7, 9, 14)
print(y)

x = min(13, 7, 9, 14)
print(x)

z = pow(4,2)
print(z)