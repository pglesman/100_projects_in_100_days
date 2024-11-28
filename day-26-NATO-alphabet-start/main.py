import pandas as pd

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet = {value.letter: value.code for index, value in data_alphabet.iterrows()}
# print(dict_alphabet)


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic_word():
    user_word = input("Enter a word: ").upper()
    try:
        user_word_list = [dict_alphabet[letter] for letter in user_word]
        print(user_word_list)
    except KeyError:
        print('Sorry, only letters in alphabet please.')
        generate_phonetic_word()


generate_phonetic_word()
