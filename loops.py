#while loop
num=20
while num <= 25:
    print(num)
    num += 1

#decrementing
print("Decrementing")
a = 10
while a >= 1:
    print(a)
    a -= 1

#Break
print("Break loop")
x=20
while x <= 25:
    print(x)
    if x == 22:
        break
    x += 1

#Continue(skipping a number)
print("Continue loop")
y=20
while y <= 25:
    y += 1
    if y == 22:
        continue
    print(y)

#For loop
print("For loop")
languages = ["python", "PHP", "kotlin"]
for x in languages:
    print(x)

#Range
print("Range")
for num in range(60, 65):
    print(num)

for z in range(1, 11, 2):
    print(z)