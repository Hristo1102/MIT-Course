'''
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("Enter a word:")
times = int(input("Enter a level:"))

i = 0
while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1

print("What das that spell?")

for i in range(times):
    print(word, "!!!")
'''

an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("Enter a word:")
times = int(input("Enter a level:"))

for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)

print("What das that spell?")

for i in range(times):
    print(word, "!!!")