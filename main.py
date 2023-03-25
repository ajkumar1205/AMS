from tkinter import *
from pathlib import Path
import os
from datetime import date
import time
from face_detection_project import detect_all
from face_recognition import recognise
from training import train

no_of_students = 0
print(time.perf_counter())

path = os.path.join(str(Path.cwd()), "attendence", "attendence.txt" )

file = open(path, 'a')
file.write(str(date.today()))

gui = Tk()
gui.geometry("300x200")
gui.title("AMS - Attendence Management System")

welcome = Label(gui, text="Welcome, Setup the System", font=("Arial", 15))
welcome.grid(row=0, column=0, columnspan=4)

enter_text = Label(gui, text="Enter the number of students", padx=5)
enter_text.grid(row=1, column=0, columnspan=2)

students = Entry(gui, width=10)
students.grid(row=1, column=2)

def get_students_and_detect():
    global no_of_students
    try:
        no_of_students = int(students.get())
        detect_all(no_of_students)
        train()
    except:
        print("Enter a Valid no of students")

submit_button = Button(gui, text="Detect it", command=get_students_and_detect)
submit_button.grid(row=1, column=3)

already = Label(gui, text="Already had Setup?", font=("Arial", 15))
already.grid(row=2, column=0, columnspan=4)

attendence = Label(gui, text="Take attendence", fg="#666")
attendence.grid(row=3, column=0, columnspan=4)

index = 1
student_number = Label(gui, text=f"Roll no {index}", fg="#ff0000", font=("Arial", 12))
student_number.grid(row=4, column=0, columnspan=3)

def check_and_mark_attendence():
    global index
    recognise(index, no_of_students)
    index = (index + 1)%no_of_students
    student_number.config(text=f"Roll no {index}")

take = Button(gui, text="Check", command=check_and_mark_attendence)
take.grid(row=4, column=2, columnspan=2)

st = Label(gui, text="Stand Closer to the camera", font=("Arial", 15))
st.grid(row=5, column=0, columnspan=4)

gui.mainloop()
print(time.perf_counter())
