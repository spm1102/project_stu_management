from typing import Any


class student_c:
    lab = "EDABK"
    lab_list = []
    
    def __init__(self, name = "", ID = 0, gpa = 0, classroom = ""):
        self.name = name
        self.ID = ID
        self.gpa = gpa
        self.classroom = classroom
        self.lab_list.append(self)
    def show_infor(self):
        print(f"{self.name :<25}{self.ID :<15}{self.classroom :<10}{self.gpa :<5}")
        
    def __lt__(self, other):
        return self.gpa < other.gpa
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    

        
    