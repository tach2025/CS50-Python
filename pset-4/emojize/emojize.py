import emoji

# Prompt user for an input
prompt = input("Input: ").strip()
print(emoji.emojize(prompt, language='alias'))
