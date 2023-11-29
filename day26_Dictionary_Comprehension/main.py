# list comprehension new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]
import random

# number = [1, 2, 3]
# new_list = [n+1 for n in number]
# print(number)

# name = input("Enter your name: ")
# new_list = [c for c in name]

# name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_list = [i for i in name if len(i) <= 4]
# new_list = [i.upper() for i in name if len(i) > 4]

# new_list = [2*n for n in range(1,5)]

# list_of_strings = input().split(',')
# cannot type change in the same list comprehension
# new_list = [int(n) for n in list_of_strings]
# new_list = [n for n in list_of_strings if n % 2 == 0]

# with open("file1.txt") as file1:
#     list1 = file1.read().split()
# with open("file2.txt") as file2:
#     list2 = file2.read().split()
# list1 = [int(n) for n in list1]
# list2 = [int(n) for n in list2]
# new_list = [n for n in list1 if n in list2]


# print(new_list)


#     ********DICTIONARY Comprehension******
# new_dict = {new_key:new_value for (key, value) in dict.items if test}

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_scores = {student: random.randint(1, 100) for student in names}
# new_dict = {student: score for (student, score) in student_scores.items() if score >= 60}

import pandas
# student_dict = {
#                 "student": ['Alex', 'Caroline', 'Dave', 'Eleanor'],
#                 "score": [56, 76, 89, 100]
#                 }
# new_dict = pandas.DataFrame(student_dict)
# for (index, row) in new_dict.iterrows():
#     print(index)
#     print(row)
#     print(row.student)
# print(new_dict)


data_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {}
for (index, row) in data_dataframe.iterrows():
    phonetic_dict[row.letter] = row.code

def generate_phonetic():
    try:
        name = input("Enter your name: ").upper()
        new_list = [phonetic_dict[n] for n in name]
    except KeyError:
        print("No number/symbols Allowed. Please enter letters only.")
        generate_phonetic()
    else:
        print(new_list)

generate_phonetic()
