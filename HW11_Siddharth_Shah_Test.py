import unittest
from HW11_Siddharth_Shah import Repositiory, Student, Instructor, Major
from typing import List,Dict
from prettytable import PrettyTable


class HW11TestCase(unittest.TestCase):
    """
    class to test the HW10 assignment
    """
    def test_students(self):
        """
        to test student
        """
        #print("starting to test")
        r:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo",r"C:\Users\12012\Desktop\Python\810\Hw11.db")
        cwid:List[str]=list()
        name:List[str]=list()
        major:List[str]=list()
        completed_courses:List[List[str]]=list()
        remaining_electives:List[List[str]]=list()
        remaining_required:List[List[str]]=list()
        gpa:List[float]=list()
        out:PrettyTable=r.student_pretty_table()
        for row in out:
            row.border=False
            row.header=False
            cwid.append(row.get_string(fields = ["Cwid"]).strip())
            name.append(row.get_string(fields = ["Name"]).strip())
            major.append(row.get_string(fields = ["Major"]).strip())
            completed_courses.append(row.get_string(fields = ["Completed Courses"]).strip())
            remaining_required.append(row.get_string(fields = ["Remaining Required"]).strip())
            remaining_electives.append(row.get_string(fields = ["Remaining Elective"]).strip())
            gpa.append(row.get_string(fields = ["GPA"]).strip())
            



        test_cwid:List[str]=['10103', '10115', '10183', '11714']
        test_name:List[str]=['Jobs, S', 'Bezos, J', 'Musk, E', 'Gates, B']
        test_major:List[str]=['SFEN', 'SFEN', 'SFEN', 'CS']
        test_cc:List[List[str]]=["['CS 501', 'SSW 810']", "['SSW 810']", "['SSW 555', 'SSW 810']", "['CS 546', 'CS 570', 'SSW 810']"]
        test_re:List[List[str]]=['[]', '[]', "['CS 501', 'CS 546']", '[]']
        test_gpa:List[float]=['3.38', '4.00', '4.00', '3.50']
        test_rr:List[List[str]]=["['SSW 540', 'SSW 555']", "['SSW 540', 'SSW 555']", "['SSW 540']", '[]']
        self.assertEqual(cwid,test_cwid)
        self.assertEqual(name,test_name)
        self.assertEqual(major,test_major)
        self.assertEqual(completed_courses,test_cc)
        self.assertEqual(remaining_required,test_rr)
        self.assertEqual(remaining_electives,test_re)
        self.assertEqual(gpa,test_gpa)
        
        # print(cwid)
        # print(name)
        # print(major)
        # print(completed_courses)
        # print(remaining_required)
        # print(remaining_electives)
        # print(gpa)
    
    def test_instructor(self)->None:
        """
        To test instructor 
        """
        r:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo",r"C:\Users\12012\Desktop\Python\810\Hw11.db")
        cwid:List[str]=list()
        name:List[str]=list()
        department:List[str]=list()
        course:List[str]=list()
        count:List[int]=list()
        out:PrettyTable=r.instructor_pretty_table()
        for row in out:
            row.border=False
            row.header=False
            cwid.append(row.get_string(fields = ["Cwid"]).strip())
            name.append(row.get_string(fields = ["Name"]).strip())
            department.append(row.get_string(fields = ["Department"]).strip())
            course.append(row.get_string(fields = ["Course"]).strip())
            count.append(row.get_string(fields = ["Count"]).strip())
        
        # print(cwid)
        # print(name)
        # print(department)
        # print(course)
        # print(count)
        test_cwid:List[str]=['98764', '98763', '98763', '98762', '98762', '98762']
        test_name:List[str]=['Cohen, R', 'Rowland, J', 'Rowland, J', 'Hawking, S', 'Hawking, S', 'Hawking, S']
        test_department:List[str]=['SFEN', 'SFEN', 'SFEN', 'CS', 'CS', 'CS']
        test_course:List[str]=['CS 546', 'SSW 810', 'SSW 555', 'CS 501', 'CS 546', 'CS 570']
        test_count:List[str]=['1', '4', '1', '1', '1', '1']
        self.assertEqual(cwid,test_cwid)
        self.assertEqual(name,test_name)
        self.assertEqual(department,test_department)
        self.assertEqual(course,test_course)
        self.assertEqual(count,test_count)
    
    def test_major(self):
        r:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo",r"C:\Users\12012\Desktop\Python\810\Hw11.db")
        major:List[str]=list()
        req_course:List[List[str]]=list()
        elec_course:List[List[str]]=list()
        out:PrettyTable=r.major_pretty_table()
        for row in out:       
            row.border=False
            row.header=False  
            major.append(row.get_string(fields = ["Major"]).strip())
            req_course.append(row.get_string(fields = ["Required Courses"]).strip())
            elec_course.append(row.get_string(fields = ["Elective Courses"]).strip())

        test_major:List[str]=['SFEN', 'CS']
        test_rc:List[List[str]]=["['SSW 540', 'SSW 810', 'SSW 555']", "['CS 570', 'CS 546']"]
        test_elec:List[List[str]]=["['CS 501', 'CS 546']", "['SSW 810', 'SSW 565']"]
        self.assertEqual(major,test_major)
        self.assertEqual(req_course,test_rc)
        self.assertEqual(elec_course,test_elec)

        # print(major)
        # print(req_course)
        # print(elec_course)
    
    def test_student_grade(self)->None:
        """
        to test the sql generated table
        """
        r:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo",r"C:\Users\12012\Desktop\Python\810\Hw11.db")
        cwid:List[str]=list()
        name:List[str]=list()
        course:List[str]=list()
        grade:List[str]=list()
        instructor:List[str]=list()
        out:PrettyTable=r.student_grades_table(r._db_path)
        for row in out:       
            row.border=False
            row.header=False  
            name.append(row.get_string(fields = ["Name"]).strip())
            cwid.append(row.get_string(fields = ["CWID"]).strip())
            course.append(row.get_string(fields = ["Course"]).strip())
            grade.append(row.get_string(fields = ["Grade"]).strip())
            instructor.append(row.get_string(fields = ["Instructor"]).strip())
        
        # print(name)
        # print(cwid)
        # print(course)
        # print(grade)
        # print(instructor)
        test_name:List[str]=['Bezos, J', 'Bezos, J', 'Gates, B', 'Gates, B', 'Gates, B', 'Jobs, S', 'Jobs, S', 'Musk, E', 'Musk, E']
        test_cwid:List[str]=['10115', '10115', '11714', '11714', '11714', '10103', '10103', '10183', '10183']
        test_course:List[str]=['SSW 810', 'CS 546', 'SSW 810', 'CS 546', 'CS 570', 'SSW 810', 'CS 501', 'SSW 555', 'SSW 810']
        test_grade:List[str]=['A', 'F', 'B-', 'A', 'A-', 'A-', 'B', 'A', 'A']
        test_instructor:List[str]=['Rowland, J', 'Hawking, S', 'Rowland, J', 'Cohen, R', 'Hawking, S', 'Rowland, J', 'Hawking, S', 'Rowland, J', 'Rowland, J']

        self.assertEqual(name,test_name)
        self.assertEqual(cwid,test_cwid)
        self.assertEqual(course,test_course)
        self.assertEqual(grade,test_grade)
        self.assertEqual(instructor,test_instructor)















if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
            








