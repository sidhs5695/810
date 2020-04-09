import unittest
from HW10_Siddharth_Shah import Repositiory, Student, Instructor, Major
from typing import List,Dict
from prettytable import PrettyTable


class HW10TestCase(unittest.TestCase):
    """
    class to test the HW10 assignment
    """
    def test_students(self):
        """
        to test student
        """
        #print("starting to test")
        r:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo")
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
            



        test_cwid:List[str]=['10103', '10115', '10172', '10175', '10183', '11399', '11461', '11658', '11714', '11788']
        test_name:List[str]=['Baldwin, C', 'Wyatt, X', 'Forbes, I', 'Erickson, D', 'Chapman, O', 'Cordova, I', 'Wright, U', 'Kelly, P', 'Morton, A', 'Fuller, E']
        test_major:List[str]=['SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SYEN', 'SYEN', 'SYEN', 'SYEN', 'SYEN']
        test_cc:List[List[str]]=["['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']", "['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']", "['SSW 555', 'SSW 567']", "['SSW 564', 'SSW 567', 'SSW 687']", "['SSW 689']", "['SSW 540']", "['SYS 611', 'SYS 750', 'SYS 800']", '[]', "['SYS 611', 'SYS 645']", "['SSW 540']"]
        test_re:List[List[str]]=['[]', '[]', "['CS 501', 'CS 513', 'CS 545']", "['CS 501', 'CS 513', 'CS 545']", "['CS 501', 'CS 513', 'CS 545']", '[]', "['SSW 540', 'SSW 565', 'SSW 810']", '[]', "['SSW 540', 'SSW 565', 'SSW 810']", '[]']
        test_gpa:List[float]=['3.44', '3.81', '3.88', '3.58', '4.00', '3.00', '3.92', '0.0', '3.00', '4.00']
        test_rr:List[List[str]]=["['SSW 540', 'SSW 555']", "['SSW 540', 'SSW 555']", "['SSW 540', 'SSW 564']", "['SSW 540', 'SSW 555']", "['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567']", "['SYS 612', 'SYS 671', 'SYS 800']", "['SYS 612', 'SYS 671']", "['SYS 612', 'SYS 671', 'SYS 800']", "['SYS 612', 'SYS 671', 'SYS 800']", "['SYS 612', 'SYS 671', 'SYS 800']"]
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
        #print(remaining_required[5])
        # print(remaining_electives)
        # print(gpa)
        #print(test_rr[5])]
    
    def test_instructor(self)->None:
        """
        To test instructor 
        """
        r:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo")
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
        
        #print(count)
        #print(course)
        test_cwid:List[str]=['98765', '98765', '98764', '98764', '98764', '98764', '98763', '98763', '98760', '98760', '98760', '98760']
        test_name:List[str]=['Einstein, A', 'Einstein, A', 'Feynman, R', 'Feynman, R', 'Feynman, R', 'Feynman, R', 'Newton, I', 'Newton, I', 'Darwin, C', 'Darwin, C', 'Darwin, C', 'Darwin, C']
        test_department:List[str]=['SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SFEN', 'SYEN', 'SYEN', 'SYEN', 'SYEN']
        test_course:List[str]=['SSW 567', 'SSW 540', 'SSW 564', 'SSW 687', 'CS 501', 'CS 545', 'SSW 555', 'SSW 689', 'SYS 800', 'SYS 750', 'SYS 611', 'SYS 645']
        test_count:List[str]=['4', '3', '3', '3', '1', '1', '1', '1', '1', '1', '2', '1']
        self.assertEqual(cwid,test_cwid)
        self.assertEqual(name,test_name)
        self.assertEqual(department,test_department)
        self.assertEqual(course,test_course)
        self.assertEqual(count,test_count)
    
    def test_major(self):
        r:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo")
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

        test_major:List[str]=['SFEN', 'SYEN']
        test_rc:List[List[str]]=["['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567']","['SYS 671', 'SYS 612', 'SYS 800']"]
        test_elec:List[List[str]]=["['CS 501', 'CS 513', 'CS 545']","['SSW 810', 'SSW 565', 'SSW 540']"]
        self.assertEqual(major,test_major)
        self.assertEqual(req_course,test_rc)
        self.assertEqual(elec_course,test_elec)

        # print(major)
        # print(req_course)
        # print(elec_course)








if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
            








