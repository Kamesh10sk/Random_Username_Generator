import random
import os

def generate_username(adjectives, nouns, use_numbers, use_special_chars, username_length):
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", ",", "_", 
    "-", "~", "`", "|", "\\", ".", "/", "°", "§", "•", "★", "☆", 
    "♥", "♣", "♦", "♠", "☼", "☾", "☻", "♪", "♫", "∞", "✓", "✗", 
    "✿", "☮", "☯", "✔", "✧", "☀", "❄", "☁", "⚡", "☂"]
    numbers = "0123456789"
    username = random.choice(adjectives).capitalize() + random.choice(nouns).capitalize()
    if use_numbers:
        username += random.choice(numbers)

    if use_special_chars:
        username += random.choice(special_characters)
    if username_length and username_length > len(username):
        additional_length = username_length - len(username)
        username += ''.join(random.choices(numbers + special_characters, k=additional_length))

    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    # Check if the specified directory exists; if not, create it
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, "w", encoding="utf-8") as file:  # Use utf-8 encoding
        for username in usernames:
            file.write(username + "\n")

def main():
    print("Welcome to the Random Username Generator!")
    adjectives = ["Wacky", "Silly", "Goofy", "Quirky", "Zany", "Crazy", 
    "Sassy", "Fluffy", "Sneaky", "Chunky", "Bouncy", "Fuzzy", 
    "Snarky", "Jumpy", "Cheeky", "Dizzy", "Clumsy", "Wobbly", 
    "Bubbly", "Giggly", "Cranky", "Perky", "Rowdy", "Stinky", 
    "Witty", "Funky", "Nifty", "Spunky", "Grumpy", "Chirpy", 
    "Prickly", "Sleepy", "Snuggly", "Chilly", "Wiggly", "Frothy", 
    "Dorky", "Soggy", "Loopy", "Zesty", "Spicy", "Breezy", 
    "Puffy", "Groovy", "Sticky", "Squeaky", "Peppy", "Frisky", 
    "Gritty", "Ducky"]

    nouns = ["Tiger", "Dragon", "Panda", "Wolf", "Eagle", "Bear",
    "Banana", "Pickle", "Waffle", "Muffin", "Nugget", "Penguin", 
    "Cactus", "Unicorn", "Squid", "Taco", "Llama", "Doughnut", 
    "Pineapple", "Pancake", "Chicken", "Monkey", "Sloth", "Octopus", 
    "Potato", "Toast", "Cheeseburger", "Meatball", "Ferret", "Turtle", 
    "Koala", "Flamingo", "Walrus",  "Carrot",  "Sausage", "Cabbage",
    "Marshmallow", "Pudding", "Shrimp", "Coconut", "Hamster", 
    "Otter", "Giraffe", "Lobster", "Snail", "Raccoon", "Duckling",
    "Pelican", "Zebra", "Butterfly", "Bee"]
    
    use_numbers = input("Include numbers in the username? (yes/no): ").strip().lower() == "yes"
    use_special_chars = input("Include special characters in the username? (yes/no): ").strip().lower() == "yes"
    username_length = input("Set a specific username length (leave blank for default): ").strip()

    if username_length.isdigit():
        username_length = int(username_length)
    else:
        username_length = None

    number_of_usernames = input("How many usernames would you like to generate? (default is 1): ").strip()

    if number_of_usernames.isdigit():
        number_of_usernames = int(number_of_usernames)
    else:
        number_of_usernames = 1

    usernames = [
        generate_username(adjectives, nouns, use_numbers, use_special_chars, username_length)
        for _ in range(number_of_usernames)
    ]

    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

    save_to_file = input("Would you like to save the usernames to a file? (yes/no): ").strip().lower() == "yes"
    if save_to_file:
        directory = input("Enter the directory where you want to save the file (or leave blank for default): ").strip()
        if directory:
            save_usernames_to_file(usernames, f"{directory}/usernames.txt")
        else:
            save_usernames_to_file(usernames)
        print("Usernames saved to usernames.txt")

if __name__ == "__main__":
    main()
