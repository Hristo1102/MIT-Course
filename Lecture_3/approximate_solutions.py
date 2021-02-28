num = int(input("Enter a number:"))

epsilon = 0.1
increment = 0.01
num_guesses = 0

guess = 0.0
while abs(guess**3 - num) >= epsilon and guess <= num:
    guess += increment
    num_guesses += 1

print('num_guesses =', num_guesses)

if abs(guess**3 - num) >= epsilon:
    print('Failed on cube root of', num, "with these parameters.")
else:
    print(guess, 'is close to the cube root of', num)