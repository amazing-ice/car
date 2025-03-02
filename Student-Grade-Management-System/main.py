from StudentManager import StudentManager
import time
import os


if __name__ == "__main__":
    os.system('cls')
    time.sleep(1)
    print('欢迎来到湖南大学学生成绩管理系统', flush=True)
    time.sleep(0.2)
    print('请按任意键继续',end='', flush=True)
    input()
    manager = StudentManager()
    time.sleep(1)
    
    while(True):
        os.system('cls')
        time.sleep(1)
        print('*********************************************', flush=True)
        time.sleep(0.3)
        print('***            请输入您的操作              ***', flush=True)
        time.sleep(0.3)
        print('***            1.添加学生信息              ***', flush=True)
        time.sleep(0.3)
        print('***            2.查询学生信息              ***', flush=True)
        time.sleep(0.3)
        print('***            3.修改学生信息              ***', flush=True)
        time.sleep(0.3)
        print('***            4.删除学生信息              ***', flush=True)
        time.sleep(0.3)
        print('***           5.显示所有学生信息            ***', flush=True)
        time.sleep(0.3)
        print('***              6.成绩统计                ***', flush=True)
        time.sleep(0.3)
        print('***              7.退出系统                ***', flush=True)
        time.sleep(0.3)
        print('*********************************************', flush=True)
        time.sleep(0.3)
        a = int(input())
        if a == 1:
            print('请输入学生姓名', flush=True)
            name = input()
            print('请输入学生ID', flush=True)
            student_id = input()
            print('请输入学生语文成绩', flush=True)
            Chinese = int(input())
            print('请输入学生数学成绩', flush=True)
            Math = int(input())
            print('请输入学生英语成绩', flush=True)
            English = int(input())
            manager.add_student(name, student_id, {'Chinese':Chinese, 'Math':Math, 'English':English})
            print("3s后自动返回初始页", flush=True)
            time.sleep(2)
        elif a == 2:
            print("请输入学生姓名/ID", flush=True)
            message = input()
            print(manager.query_student(message), flush=True)
            print("3s后自动返回初始页", flush=True)
            time.sleep(2)
        elif a == 3:
            print("请输入学生ID", flush=True)
            student_id = input()
            
            student = manager.query_student(student_id)
            if student is None:
                continue
            
            print("找到学生：", student, flush=True)
            time.sleep(0.3)
            print("请输入你要修改的类型", flush=True)
            time.sleep(0.3)
            print("1. 姓名", flush=True)
            time.sleep(0.3)
            print("2. 语文成绩", flush=True)
            time.sleep(0.3)
            print("3. 数学成绩", flush=True)
            time.sleep(0.3)
            print("4. 英语成绩", flush=True)
            time.sleep(0.3)
            print("5. 选择完毕", flush=True)
            time.sleep(0.3)
            
            modifications = {}
            while True:
                choice = input("请输入修改类型编号：")
                time.sleep(0.3)
                if choice == '1':
                    print("请输入新的姓名", flush=True)
                    new_name = input()
                    modifications['name'] = new_name
                elif choice == '2':
                    print("请输入新的语文成绩", flush=True)
                    new_chinese = int(input())
                    modifications['grades'] = {'Chinese': new_chinese} if 'grades' not in modifications else {**modifications['grades'], 'Chinese': new_chinese}
                elif choice == '3':
                    print("请输入新的数学成绩", flush=True)
                    new_math = int(input())
                    modifications['grades'] = {'Math': new_math} if 'grades' not in modifications else {**modifications['grades'], 'Math': new_math}
                elif choice == '4':
                    print("请输入新的英语成绩", flush=True)
                    new_english = int(input())
                    modifications['grades'] = {'English': new_english} if 'grades' not in modifications else {**modifications['grades'], 'English': new_english}
                elif choice == '5':
                    break
                else:
                    print("无效的选择，请重新输入", flush=True)
            
            if modifications:
                manager.modify_student(student_id, **modifications)

                student = manager.query_student(student_id)
                print("已将学生信息修改为：\n", student, flush=True)
            
            print("3s后自动返回初始页", flush=True)
            time.sleep(2)
        elif a==4:
            print("请输入要删除学生的ID", flush=True)
            student_id = input()
            manager.delete_student(student_id)
            print("3s后自动返回初始页", flush=True)
            time.sleep(2)
        elif a==5:
            print("请输入排序方式", flush=True)
            print("1.ID排序 2.总分排序", flush=True)
            choice = input()
            manager.display_students(choice)
            print("3s后自动返回初始页", flush=True)
            time.sleep(2)
        elif a==6:
            manager.statistics()
            print("3s后自动返回初始页", flush=True)
            time.sleep(2)
        elif a==7:
            print("再见", flush=True)
            time.sleep(1)
            break
        else:
            print("无效的选择，请重新输入", flush=True)
            print("3s后自动返回初始页", flush=True)
            time.sleep(2)