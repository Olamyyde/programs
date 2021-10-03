from types import resolve_bases


name = "same"

print([x for x in name])


names = ["sar", "dark", "office"]

print([x for x in names if len(x)>3])
print([x.upper() for x in names if len(x)>3])


nos = [1,2,3,4,5]

sq_nos = [x**2 for x in nos]
even_nos = [x for x in nos if x%2==0]

print(sq_nos)
print(even_nos)


# comparing values in a file
with open("file1.txt") as f1:
    file1_data = f1.readlines()

with open("file2.txt") as f2:
    file2_data = f2.readlines()

result = [int(i) for i in file1_data if i in file2_data]
print(result)


names = ["sam", "dave", "james", "tyrel", "Quadri"]
import random
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score>40}
print(passed_students)

# Splitting a word, orint it and the index with a list comprehension
sentence = "say what you wanna say"

result = {word:len(word) for word in sentence.split()}

print(result)


# Weather Converter
weather_c ={
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
}



# temp_c = [temp for key, temp in weather_c.items()]
# print(temp_c)

# temp_f = (temp_c * 9/5) + 32

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)


# DataFrame

student_dict = {
    "stuudent": ["Angela", "James", "Lily"],
    "Score": [56, 76, 98]
}

# Looping tru dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)


# loop tru each of the rows of the dataframe
for (index, row) in student_df.iterrows():
    print(row.stuudent)
    print(row.score)

