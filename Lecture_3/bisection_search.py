num = int(input("Enter a number:"))

epsilon = 0.1
num_guesses = 0
low = 0
high = num

guess = (high + low)/2.0
while abs(guess**3 - num) >= epsilon:
    if guess**3 < num:
        low = guess
    else:
        high = guess

    guess = (high + low)/2.0
    num_guesses += 1

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', num)