import pandas as pd
student_data = [{"name": "a", "class": 1, "score": 90},
 {"name": "b", "class": 1, "score": 85},
 {"name": "c", "class": 1, "score": 50},
 {"name": "d", "class": 1, "score": 90}, 
 {"name": "a", "class": 2, "score": 50},
 {"name": "b", "class": 2, "score": 30},
 {"name": "c", "class": 2, "score": 70},
 {"name": "d", "class": 2, "score": 60}]

student_dataframe = pd.DataFrame(student_data)
final_data = student_dataframe[student_dataframe["score"]>50]
print(final_data)
student_dataframe[["class", "score"]]
final_data = student_dataframe[["class", "score"]].groupby(['class']).mean()

print(final_data)

# student_data.find("name"="a" or "name"="b")


# Select * from student_data
# where dob is null;