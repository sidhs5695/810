"""
Program that works on student and instructor repositiories
"""
from typing import Dict,List,DefaultDict, Set
from collections import defaultdict
from HW08_Siddharth_Shah import file_reader
from prettytable import PrettyTable
import os,sys
class Student:
    """
    creating instance of a student
    """
    field_name:List[str]=["Cwid","Name","Major","Courses"]
    def __init__(self,cwid:str,name:str,major:str)->None:
        """
        dunder method to initialize fields related to student
        """
        self._cwid:str=cwid
        self._name:str=name
        self._major:str=major
        self._courses:Dict[str,str]=dict()
    
    def courses_add(self,course:str,grade:str)->None:
        """
        method to add courses for each student in dictionary
        """
        self._courses[course]=grade
    
    def info(self)->List[str]:
        return [self._cwid,self._name,self._major,sorted(self._courses.keys())]

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
        self._setcourse:Set=set()
        self._courses:DefaultDict[str,int]=defaultdict(int)

    def inst_courses_add(self, course:str)->None:
        """
        method to add course name and count of students
        """
        self._setcourse.add(course)
        self._courses[course]+=1
    
    def info(self)->List[str]:
        return [self._cwid,self._name,self._dept]
    
class Repositiory:
    """
    class to create a repository of student and instructor of a university
    """
    def __init__(self,path:str)->None:

        self._path:str=path
        self._students:Dict[str,Student]=dict()
        self._instructors:Dict[str,Instructor]=dict()
        self._read_students()
        self._read_instructors()
        self._read_grades()        
        self.student_pretty_table()
        self.instructor_pretty_table()
        
    
    def _read_students(self)->None:
        """
        Reading each student and creating instances of each as soon as it is read
        """
        try:
            for cwid, name, major in file_reader(os.path.join(self._path,"students.txt"), 3, sep='\t',header=False):
                if cwid in self._students:
                    raise KeyError("Student with CWID is already in the file")
                self._students[cwid]=Student(cwid,name,major)
        except FileNotFoundError:
            raise FileNotFoundError(f"Cannot open file at {self._path}")
        except ValueError:
            raise ValueError("Missing field")
        
        
    def _read_instructors(self)->None:
        """
        Reading each instructor and crating instances as soon as it is read
        """
        try:
            for cwid, name, dept in file_reader(os.path.join(self._path,"instructors.txt"), 3, sep='\t', header=False):
                if cwid in self._instructors:
                    raise KeyError("Instructor with CWID is already in the file")
                self._instructors[cwid]=Instructor(cwid,name,dept)
        except (FileNotFoundError, ValueError) as e:
            raise FileNotFoundError(f"Cannot open file at {self._path}")
        except ValueError:
            raise ValueError("Missing field")
            

    

    def _read_grades(self)->None:
        """
        Reading grade of each student 
        """
        try:
            for stud_cwid, course, grade, prof_cwid in file_reader(os.path.join(self._path,"grades.txt"), 4, sep='\t', header=False):
                if stud_cwid in self._students:
                    s:Student=self._students[stud_cwid] #handle the key error if a new student 
                else:
                    raise KeyError(f"No such Student with {stud_cwid}")
                if stud_cwid in self._students:
                    p:Instructor=self._instructors[prof_cwid] #handle the key error if a new instructor
                else:
                    raise KeyError(f"No such Student with {prof_cwid}")
                s.courses_add(course,grade)
                p.inst_courses_add(course) 
        except FileNotFoundError:
            raise FileNotFoundError(f"Cannot open file at {self._path}")
        except ValueError:
            raise ValueError("Wrong input")
            
        
    def student_pretty_table(self)->None:
        """
        Creating a pretty table of Student
        """
        pt:PrettyTable=PrettyTable()
        pt.field_names=Student.field_name
        for s in self._students.values():
            pt.add_row(s.info())
        print(pt)
    
    def instructor_pretty_table(self)->None:
        """
        Creating a pretty table of Instructor
        """
        pt:PrettyTable=PrettyTable()
        pt.field_names=Instructor.field_name
        for s in self._instructors.values():
            for i in s._setcourse:
                temp:List[str]=[i,s._courses[i]]
                output:List[str]=s.info()
                output.extend(temp)
                pt.add_row(output)
        print(pt)
    
def main():
    stevens:Repositiory=Repositiory("C:\\Users\\12012\\Desktop\\Python\\810\\Stevens_repo")#use r for eliminating //
       
main()
