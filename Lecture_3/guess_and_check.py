'''
num = int(input("Enter a number:"))

count = 0
while count**3 < abs(num):
    count += 1
if count**3 == abs(num):
    print(count, "is the cube root of", num)
else:
    print(num, "doesnt have a perfect cube root")
'''

num = int(input("Enter a number:"))

for guess in range(abs(num)):
    if guess**3 >= abs(num):
        break

if guess**3 != abs(num):
    print(num, 'is not a perfect cube')
else:
    if num < 0:
        guess = -guess
    print('Cube root of ' + str(num) + ' is ' + str(guess))