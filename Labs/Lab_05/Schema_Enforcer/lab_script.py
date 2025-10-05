# HINT: Use the 'csv' module with 'writer' or 'DictWriter', 
# or just simple Python file I/O with .write() to save the data.
# Be sure to include headers in your first row!

import csv
import json
import pandas as pd

# Creating raw CSV
data = [
    ['student_id', 'major', 'GPA', 'is_cs_major', 'credits_taken'],
    [5, 'cs', 2.0, True, '98'],
    [6, 'psych', 3, 'No', 56],
    [1, 'ds', 3.2, False, '48'],
    [2, 'cs', 4, 'Yes', 17],
    [3, 'ece', 3.6, False, 115]
]

with open('raw_survey_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)


# Creating raw JSON
json_data = [
  {
    "course_id": "DS2002",
    "section": "001",
    "title": "Data Science Systems",
    "level": 200,
    "instructors": [
      {"name": "Austin Rivera", "role": "Primary"}, 
      {"name": "Heywood Williams-Tracy", "role": "TA"} 
    ]
  },
  {
    "course_id": "CS3100",
    "title": "Data Structures and Algorithms 2",
    "section": "001",
    "level": 300,
    "instructors": [
      {"name": "Aaron Bloomfield", "role": "Primary"}
    ]
  },
  {
    "course_id": "CS3710",
    "section": "001",
    "title": "Intro to Cybersecurity",
    "level": 300,
    "instructors": [
      {"name": "Angela Orebaugh", "role": "Primary"}
    ]
  }
]

with open("raw_course_catalog.json", "w") as f:
    json.dump(json_data, f)

# Cleaning the survey data
df = pd.read_csv('raw_survey_data.csv')
df['is_cs_major'] = df['is_cs_major'].replace({'Yes': True, 'No': False})
df['GPA'] = df['GPA'].astype(float)
df['credits_taken'] = df['credits_taken'].astype(float)
df.to_csv('clean_survey_data.csv', index=False)

# Cleaning JSON data
with open("raw_course_catalog.json", "r") as f:
    courses = json.load(f)

courses_df = pd.json_normalize(courses, record_path=['instructors'], meta=['course_id', 'title', 'level'])
courses_df.to_csv('clean_course_catalog.csv', index=False)

