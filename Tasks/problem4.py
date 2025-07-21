# 1
# This script prompts the user for their name and greets them.
name = input("Enter your name: ")
print(f"Good Morning farigh {name}!") # Using f before strings, you can print variable in the string directly.
# 2
# Insert name and date in a letter.
letter = '''Dear {name}
you are selected!
Date: {date}
Thank you!'''
print(letter.replace("{name}", "Musaab").replace("{date}","03/10/2022"))