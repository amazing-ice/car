from typing import Dict

class Student:
    def __init__(self, name: str, student_id: str, grades: Dict[str, int] = None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades else {}
        self.total_scores = sum(grades.values())
 
    def change_grade(self, course: str, score: int):
        self.grades[course] = score
 
    def __repr__(self):
        return f"姓名: {self.name}, 学号: {self.student_id}, 成绩: {self.grades}, 总分: {self.total_scores}"