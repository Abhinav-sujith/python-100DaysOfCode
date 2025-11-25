#TODO 1. Create a dictionary in this format:
import pandas as pd
df = pd.read_csv("nato_alphabet.csv")


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_dict = {row.letter: row.code for (index,row) in df.iterrows()}
word = input("What is your Name").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)


"""student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}"""


# letter = name.split()
# for single in letter:
#     if single == nato_dict.row.code:
#         print(f"{single}:{}")
