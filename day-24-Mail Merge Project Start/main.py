# Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt", mode="r") as l_file:
    letter = l_file.readlines()

# for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", mode="r") as n_file:
    names = n_file.read().split()

for name in names:
    # Replace the [name] placeholder with the actual name.
    new_letter = [letter[0].replace("[name]", name)] + letter[1:]

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as w_file:
        w_file.writelines(new_letter)

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
