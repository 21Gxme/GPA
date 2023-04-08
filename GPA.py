import tkinter as tk
from tkinter import ttk


class GPA_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("GPA Calculator")
        self.master.geometry("400x300")
        self.master.minsize(400, 300)

        self.subjects = []
        self.credits = []
        self.grades = []

        # create subject entry fields
        tk.Label(self.master, text="Subject").grid(row=0, column=0)
        tk.Label(self.master, text="Credit").grid(row=0, column=1)
        tk.Label(self.master, text="Grade").grid(row=0, column=2)

        for i in range(1, 11):
            subject_entry = tk.Entry(self.master, width=12)
            subject_entry.grid(row=i, column=0)
            credit_entry = tk.Entry(self.master, width=7)
            credit_entry.grid(row=i, column=1)

            # create drop-down menu for grade options
            grade_options = ["", "A (4.00)", "B+ (3.50)", "B (3.00)",
                             "C+ (2.50)", "C (2.00)", "D+ (1.50)", "D (1.00)",
                             "F (0.00)"]
            grade_var = tk.StringVar(value=grade_options[0])
            grade_menu = ttk.Combobox(self.master, values=grade_options,
                                      width=7,
                                      textvariable=grade_var)
            grade_menu.grid(row=i, column=2)

            self.subjects.append(subject_entry)
            self.credits.append(credit_entry)
            self.grades.append(grade_menu)

        # create calculate button
        calculate_button = tk.Button(self.master, text="Calculate GPA",
                                     command=self.calculate_gpa)
        calculate_button.grid(row=11, column=1)

        # create GPA display label
        self.gpa_label = tk.Label(self.master, text="")
        self.gpa_label.grid(row=12, column=1)

        # configure columns and rows to expand with the window
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(0, weight=1)
        for i in range(1, 11):
            self.master.rowconfigure(i, weight=1)
        self.master.rowconfigure(11, weight=1)
        self.master.rowconfigure(12, weight=1)

    def calculate_gpa(self):
        total_credits = 0
        total_grade_points = 0

        for i in range(10):
            credit_str = self.credits[i].get()
            grade_str = self.grades[i].get()

            if credit_str and grade_str:
                credit_hours = float(credit_str)
                grade = self.convert_grade(grade_str)
                total_credits += credit_hours
                total_grade_points += credit_hours * grade

        if total_credits > 0:
            gpa = round(total_grade_points / total_credits, 2)
            self.gpa_label.config(text=f"Your GPA is {gpa}")

    @staticmethod
    def convert_grade(grade_str):
        if grade_str == "A (4.00)":
            return 4.00
        elif grade_str == "B+ (3.50)":
            return 3.50
        elif grade_str == "B (3.00)":
            return 3.00
        elif grade_str == "C+ (2.50)":
            return 2.50
        elif grade_str == "C (2.00)":
            return 2.00
        elif grade_str == "D+ (1.50)":
            return 1.50
        elif grade_str == "D (1.00)":
            return 1.00
        elif grade_str == "F (0.00)":
            return 0.00
        elif grade_str == "":
            return None
        raise ValueError("Invalid grade")


root = tk.Tk()
GPA_Calculator(root)
root.mainloop()
