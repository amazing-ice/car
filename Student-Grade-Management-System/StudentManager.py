import pandas as pd
from Student import Student
from typing import Dict, Any

class StudentManager:
    def __init__(self, filename: str = "students.xlsx"):
        self.students = []
        self.filename = filename
        self._load_from_file()
 
    def _load_from_file(self):
        # 读取Excel文件
        df = pd.read_excel(self.filename, sheet_name='Sheet1')
        df['id'] = df['id'].astype(str)
        row_dicts = df.to_dict(orient='records')
        self.students = [Student(student['name'], student['id'], {key: student[key] for key in ['Chinese', 'Math', 'English']})for student in row_dicts]

    def _save_to_file(self):
        row_dicts_ = [{'name':student.name, 'id':student.student_id, 'Chinese':student.grades['Chinese'], 'Math':student.grades['Math'], 'English':student.grades['English']}for student in self.students]
        df_ = pd.DataFrame(row_dicts_)
        df_.to_excel('students.xlsx', index=False)

    def add_student(self, name: str, student_id: str, grades: Dict[str, int]):
        for student in self.students:
            if student.student_id == student_id:
                print("学号重复，请重新输入！", flush=True)
                return
        self.students.append(Student(name, student_id, grades))
        self._save_to_file()
        print("添加成功", flush=True)

    def query_student(self, query: str) -> Student:
        for student in self.students:
            if student.student_id == query or student.name == query:
                return student
        print("未找到！", flush=True)
        return None
 
    def modify_student(self, student_id: str, **kwargs: Any):
        for student in self.students:
            if student.student_id == student_id:
                if "name" in kwargs:
                    student.name = kwargs["name"]
                if "grades" in kwargs:
                    student.grades.update(kwargs["grades"])
                student.total_scores = sum(student.grades.values())
                self._save_to_file()
                return
        print("未找到！", flush=True)
 
    def delete_student(self, student_id: str):
        self.students = [student for student in self.students if student.student_id != student_id]
        self._save_to_file()
        print("已成功删除目标学生信息", flush=True)
 
    def display_students(self, sort_by: str):
        # ID排序
        if sort_by == "1":
            print("根据学生ID排序结果如下：", flush=True)
            self.students.sort(key=lambda x: x.student_id)
        # 总分排序
        elif sort_by == "2":
            print("根据学生总分排序结果如下：", flush=True)
            self.students.sort(key=lambda x: x.total_scores, reverse=True)
        else:
            raise ValueError("无效的排序方式！")
 
        for student in self.students:
            print(student)
 
    def statistics(self):
        if not self.students:
            print("没有学生数据！", flush=True)
            return
 
        total_scores = []
        for student in self.students:
            total_scores.append(sum(student.grades.values()))
 
        average_score = sum(total_scores) / len(total_scores)
        max_score = max(total_scores)
        min_score = min(total_scores)
 
        print(f"全班平均成绩: {average_score:.2f}", flush=True)
        print(f"最高分: {max_score}", flush=True)
        print(f"最低分: {min_score}", flush=True)