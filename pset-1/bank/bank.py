# Prompts the user, and then convert to lowercase
prompt = input("Greeting: ").strip().lower()

# Check the greeting conditions
if prompt.startswith("hello"):
    print("$0")
elif prompt.startswith("h"):
    print("$20")
else:
    print("$100")
