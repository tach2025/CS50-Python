# Main function
def main():
    # Prompt the user for a message
    prompt = input()
    # Print the converted prompt- from emoticons to emoji
    print(convert(prompt))


# Converts emoticons to emoji
def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


# Call the main function
main()
