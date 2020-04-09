""""
Program to work on dates, file reading and os operations
"""
from typing import Tuple,Iterator,List,IO
from datetime import datetime
from datetime import date
from datetime import timedelta
#from prettytable import PrettyTable
from prettytable import PrettyTable
import os

# def date_arithmatic()->Tuple[datetime,datetime,int]:
#     """
#     A function to find 3 days after a particular date and no of days in between 2 dates
#     """
#     three_days_after_02272020:datetime=datetime.strptime("02/27/2020","%m/%d/%Y")+timedelta(days=3)
#     three_days_after_02272019:datetime=datetime.strptime("02/27/2019","%m/%d/%Y")+timedelta(days=3)
#     days_diff:int=(datetime.strptime("09/30/2019", "%m/%d/%Y")-datetime.strptime("02/01/2019", "%m/%d/%Y")).days
#     return three_days_after_02272020, three_days_after_02272019, days_diff

def file_reader(path:str,fields:int,sep:str=",",header:bool=False)->Iterator[Tuple[str]]:
    """
    Function to implement a generator that will yield new line of a file on call of next
    """
    try:
        fp:IO=open(path,'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot open file at {path} ") #cannot open file error     
        
    else:
        counter:int=0
        for line in fp:
            row:List[str]=line.strip().split(sep)
            counter+=1
            if len(row) != fields or KeyError is True:
                fp.close()
                raise ValueError(f"File {path} at line {counter} has {len(row)} items, whereas the expected items where {fields} ")
            else:
                if header == True and counter == 1:
                    continue
                elif header == True and counter>1:
                    yield tuple(row)
                else:
                    yield tuple(row)
    fp.close()
            
# class FileAnalyzer:
#     """
#     Class to work with scanning of files, 
#     """
#     def __init__(self,directory:str)->None:
#         self.directory:str=directory
#         self.files_summary:Dict[str,Dict[str,int]] = dict()
#         self.analyze_files()
    
#     def analyze_files(self)->None:
#         """
#         Function to analyse the python files and populate the data into dictionary
#         """
#         files:List[str]=os.listdir(self.directory)
#         for i in files:
#             if(i.endswith(".py")):
#                 try:
#                     file:IO=open(os.path.join(self.directory,i),'r')
#                 except FileNotFoundError:
#                     raise FileNotFoundError(f"File {i} cannot be openend")
#                 else:
#                     #no_of_class:int=0
#                     #no_of_methods:int=0
#                     #no_of_char:int=0
#                     #num_lines:int=0
#                     num_lines:int=sum(1 for line in file)
#                     #print("before entering this loop")
#                 file.close()
#                 try:
#                     file1:IO=open(os.path.join(self.directory,i),'r')
#                 except FileNotFoundError:
#                     raise FileNotFoundError(f"File {i} cannot be openend")
#                 else:
#                     no_of_char:int=0
#                     for line in file1:   
#                         rows:List[str]=line.strip().split('\n')
#                         for word in rows:
#                             #print("counting characters")
#                             no_of_char+=len(word)
#                 file1.close()
#                 try:
#                     file2:IO=open(os.path.join(self.directory,i),'r')
#                 except FileNotFoundError:
#                     raise FileNotFoundError(f"File {i} cannot be openend")
#                 else:
#                     no_of_class:int=0
#                     no_of_methods:int=0
#                     for line in file2:
#                         rows:List[str]=line.strip().split('\n')
#                         for word in rows:
#                             if word.startswith('def'):
#                                 #print("counting functions")
#                                 no_of_methods+=1
#                             elif word.startswith('class'):
#                                 #print("counting functions")
#                                 no_of_class+=1
#                             else:
#                                 continue
#                 file2.close()
#                 self.files_summary[i]={"class":no_of_class,"method":no_of_methods,"lines":num_lines,"Character":no_of_char}
            
#     def pretty_print(self)->None:
#         """
#         Function to print the summarized detail into a table using prettytable module
#         """
#         output:object = PrettyTable()
#         output.field_names=["File Name","Class","Method","Lines","Characters"]
#         for i,j in self.files_summary.items():
#             output.add_row([i,j["class"],j["method"],j["lines"],j["Character"]])
#         return output

# x=FileAnalyzer(r"C:\Users\12012\Desktop\Python\810\test")
#print(x.pretty_print())

#print(list(file_reader("C:\\Users\\12012\\Desktop\\Python\\810\\HW_08_Siddharth_Shah.txt", 3, sep='|')))



    



    
