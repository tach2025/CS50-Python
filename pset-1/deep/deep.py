# Prompt the user and lower case the prompt
prompt = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# Check if the input is 42, forty-two or forty two
if prompt == "42" or prompt == "forty two" or prompt == "forty-two":
    print("Yes")
else:
    print("No")
