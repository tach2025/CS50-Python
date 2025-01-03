# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

prompt = input("Input: ")
print("Output: ", end='')
for i in prompt:
    if i.lower() not in vowels:
        print(i, end='')
