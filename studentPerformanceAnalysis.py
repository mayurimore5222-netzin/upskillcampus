import pandas as pd
import numpy as np

print("====================================")
print("   STUDENT PERFORMANCE ANALYSIS")
print("====================================")

# Number of students
n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter Student Name: ")

    math = float(input("Enter Math Marks: "))
    science = float(input("Enter Science Marks: "))
    english = float(input("Enter English Marks: "))
    computer = float(input("Enter Computer Marks: "))

    attendance = float(input("Enter Attendance (%): "))

    students.append([
        name, math, science, english, computer, attendance
    ])

# Create DataFrame
df = pd.DataFrame(
    students,
    columns=[
        "Name",
        "Math",
        "Science",
        "English",
        "Computer",
        "Attendance"
    ]
)

# Calculate Total using Pandas
df["Total"] = df[
    ["Math", "Science", "English", "Computer"]
].sum(axis=1)

# Calculate Percentage
df["Percentage"] = (df["Total"] / 400) * 100

# Calculate Average using NumPy
df["Average"] = np.mean(
    df[["Math", "Science", "English", "Computer"]],
    axis=1
)

# Result
df["Result"] = np.where(
    df["Percentage"] >= 40,
    "Pass",
    "Fail"
)

# Display result
print("\n====================================")
print("        STUDENT RESULT")
print("====================================")

print(df.to_string(index=False))

# Highest scorer
highest_index = df["Percentage"].idxmax()

print("\n====================================")
print("          HIGHEST SCORER")
print("====================================")

print("Name       :", df.loc[highest_index, "Name"])
print("Percentage :", df.loc[highest_index, "Percentage"], "%")

# Class average
class_average = np.mean(df["Percentage"])

print("\nClass Average :", round(class_average, 2), "%")

# Average attendance
attendance_average = np.mean(df["Attendance"])

print("Average Attendance :", round(attendance_average, 2), "%")