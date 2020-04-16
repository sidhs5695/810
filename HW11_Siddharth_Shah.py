"""
Program that works on student and instructor repositiories
"""
from typing import Dict,List,DefaultDict, Set
from collections import defaultdict
from HW08_Siddharth_Shah import file_reader
from prettytable import PrettyTable
import os,sys
import sqlite3

class Major:
    """
    Class to create instance of a major
    """
    field_name:List[str]=["Major","Required Courses","Elective Courses"]
    def __init__(self,major:str):
        """
        to initialize the instance variables
        """
        self._major:str=major
        self._required:List[str]=list()
        self._electives:List[str]=list()
    
    def add_course(self,rore:str,course:str)->None:
        """
        function to add courses and req/elective 
        """
        if rore=="R":
            self._required.append(course)
        elif rore=="E":
            self._electives.append(course)
        else:
            pass
        
    def get_required(self)->None:
        """
        function to return a copy of required courses
        """
        return list(self._required)
    
    def get_electives(self)->None:
        """
        function to return a copy of elective courses
        """
        return list(self._electives)
    
    def info(self)->List[str]:
        """
        Function to return list of ouputs
        """
        return [self._major,self._required,self._electives]

class Student:
    """
    creating instance of a student
    """
    field_name:List[str]=["Cwid","Name","Major","Completed Courses","Remaining Required","Remaining Elective","GPA"]
    _fail:List[str]=["C-","D+","D","D-","F"]
    _grade:Dict[str,float]={"A":4.0,"A-":3.75,"B+":3.25,"B":3.0,"B-":2.75,"C+":2.25,"C":2.0,"C-":0.0,"D+":0.0,"D":0.0,"D-":0.0,"F":0.0}
    def __init__(self,cwid:str,name:str,major:str,required:List[str],electives:List[str])->None:
        """
        dunder method to initialize fields related to student
        """
        self._cwid:str=cwid
        self._name:str=name
        self._major:str=major
        self._courses:Dict[str,str]=dict()
        self._remaining_required:List[str]=required
        self._remaining_electives:List[str]=electives
        #self._fail:List[str]=["C-","D+","D","D-","F"]
        #self._grade:Dict[str,float]={"A":4.0,"A-":3.75,"B+":3.25,"B":3.0,"B-":2.75,"C+":2.25,"C":2.0,"C-":0.0,"D+":0.0,"D":0.0,"D-":0.0,"F":0.0}

    def compute_gpa(self)->float:
        """
        Function to calculate gpa
        """
        sumGpa:List[float]=list()
        for i in self._courses.values():
            if i in Student._grade:
                sumGpa.append(self._grade[i])
            else:
                print("Invalid grade")
        if len(sumGpa) == 0:
            return 0.0
        else:
            gpa:float=sum(sumGpa)/len(sumGpa)
        return format(gpa,'.2f')
    
    def courses_add(self,course:str,grade:str)->None:
        """
        method to add courses for each student in dictionary
        """
        if grade not in Student._fail:
            self._courses[course]=grade
        if course in self._remaining_required:
            self._remaining_required.remove(course)
        if course in self._remaining_electives:
            self._remaining_electives.clear()
            
    def info(self)->List[str]:
        return [self._cwid,self._name,self._major,sorted(self._courses.keys()),sorted(self._remaining_required),sorted(self._remaining_electives),self.compute_gpa()]

class Instructor:
    """
    creating instance of an instructor
    """
    field_name:List[str]=["Cwid","Name","Department","Course","Count"]
    def __init__(self,cwid:str,name:str,dept:str)->None:
        """
        dunder method to initialize fields relevant to instructor
        """
        self._cwid:str=cwid
        self._name:str=name
        self._dept:str=dept
        #self._setcourse:Set=set()
        self._courses:DefaultDict[str,int]=defaultdict(int)

    def inst_courses_add(self, course:str)->None:
        """
        method to add course name and count of students
        """
        self._courses[course]+=1
    
    def info(self)->List[str]:
        for i,j in self._courses.items():
            yield[self._cwid,self._name,self._dept,i,j]
    
class Repositiory:
    """
    class to create a repository of student and instructor of a university
    """
    def __init__(self,path:str,db_path:str)->None:
        self._db_path:str=db_path
        self._path:str=path
        self._students:Dict[str,Student]=dict()
        self._instructors:Dict[str,Instructor]=dict()
        self._majors:Dict[str,Major]=dict()
        self._read_majors()
        self._read_students()
        self._read_instructors()
        self._read_grades()    
        self.major_pretty_table()    
        self.student_pretty_table()
        self.instructor_pretty_table()
        self.student_grades_table(db_path)
        
    
    def _read_majors(self)->None:
        """
        Reading each major and creating its instance
        """
        try:
            for major, rore, course in file_reader(os.path.join(self._path,"majors.txt"), 3, sep='\t', header=True):
                if major not in self._majors:
                    self._majors[major]=Major(major)
                self._majors[major].add_course(rore,course)
        except FileNotFoundError:
            print(f"Cannot open file at{self._path}")
    
    def _read_students(self)->None:
        """
        Reading each student and creating instances of each as soon as it is read
        """
        try:
            for cwid, name, major in file_reader(os.path.join(self._path,"students.txt"), 3, sep='\t',header=True):
                if cwid in self._students:
                    print("Student with CWID is already in the file")
                required:List[str]=self._majors[major].get_required()
                electives:List[str]=self._majors[major].get_electives()
                self._students[cwid]=Student(cwid,name,major,required,electives)
        except FileNotFoundError:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Missing field")
        
        
    def _read_instructors(self)->None:
        """
        Reading each instructor and crating instances as soon as it is read
        """
        try:
            for cwid, name, dept in file_reader(os.path.join(self._path,"instructors.txt"), 3, sep='\t', header=True):
                if cwid in self._instructors:
                    print("Instructor with CWID is already in the file")
                self._instructors[cwid]=Instructor(cwid,name,dept)
        except (FileNotFoundError, ValueError) as e:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Missing field")
            

    

    def _read_grades(self)->None:
        """
        Reading grade of each student 
        """
        check:bool=True
        try:
            for stud_cwid, course, grade, prof_cwid in file_reader(os.path.join(self._path,"grades.txt"), 4, sep='\t', header=True):
                if stud_cwid in self._students:
                    s:Student=self._students[stud_cwid] #handle the key error if a new student 
                else:
                    check=False
                    print(f"No such Student with {stud_cwid}")
                if prof_cwid in self._instructors:
                    p:Instructor=self._instructors[prof_cwid] #handle the key error if a new instructor
                else:
                    check=False
                    print(f"No such instructor with {prof_cwid}")
                if check:
                    s.courses_add(course,grade)
                    p.inst_courses_add(course) 
        except FileNotFoundError:
            print(f"Cannot open file at {self._path}")
        except ValueError:
            print("Wrong input")
    
    def major_pretty_table(self)->PrettyTable:
        """
        Creating a pretty table
        """
        pt:PrettyTable=PrettyTable()
        pt.field_names=Major.field_name
        for s in self._majors.values():
            pt.add_row(s.info())
        #print(pt)
        return pt
            
        
    def student_pretty_table(self)->PrettyTable:
        """
        Creating a pretty table of Student
        """
        pt:PrettyTable=PrettyTable()
        pt.field_names=Student.field_name
        for s in self._students.values():
            pt.add_row(s.info())
        #print(pt)
        return pt
    
    def instructor_pretty_table(self)->PrettyTable:
        """
        Creating a pretty table of Instructor
        """
        pt:PrettyTable=PrettyTable()
        pt.field_names=Instructor.field_name
        # for s in self._instructors.values():
        #     for i in s._setcourse:
        #         temp:List[str]=[i,s._courses[i]]
        #         output:List[str]=s.info()
        #         output.extend(temp)
        #         pt.add_row(output)
        for instval in self._instructors.values():
            for row in instval.info():
                pt.add_row(row)
        #print(pt)
        return pt

    def student_grades_table(self,db_path)->PrettyTable:
        """
        Printing the query into a pretty table
        """
        pt:PrettyTable=PrettyTable()
        pt.field_names=["Name","CWID","Course","Grade","Instructor"]
        try:
            db:sqlite3.Connection=sqlite3.connect(db_path)
        except sqlite3.OperationalError as e:
            print(e)
        else:
            try:         
                for tup in db.execute("select s.Name, s.CWID, g.Course,  g.Grade, i.Name from students s join grades g on s.CWID=StudentCWID join instructors i on InstructorCWID=i.CWID order by s.Name"):
                    pt.add_row(tup)
            except sqlite3.Error as e:
                print(e)
        #print(pt)
        return pt
    
def main():
    stevens:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo",r"C:\Users\12012\Desktop\Python\810\Hw11.db")#use r for eliminating //
       
main()