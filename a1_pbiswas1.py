#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_pbiswas1.py (replace [Seneca_name] with your Seneca User name)
Author: "PRANGON BISWAS"
The python code in this file (a1_pbiswas1.py) is original work written by
"PRANGON BISWAS". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    '''
    It checks "obj" that if it is a leap year. 
    It displays "True" if it is a leap year and "False" if it is not a leap year.
    '''
    status = False
    year = int(obj)
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               status= True
           else:
               status = False
       else:
           status = True
    else:
        status = False
    return status

def sanitize(obj1,obj2):
    '''
    It checks all characters of "obj1" and if it is in "obj2".
    It displays "status" string and then returns it.
    '''
    results = ''
    #iterate through each char in obj1
    for i in obj1:
        #if that char is in obj2 then append it to result
        if i in obj2:
            results +=i
    return results

def size_check(obj, intobj):
    '''
    It checks the size of "obj" if it is same as "intobj"
    It displays "True" if it is same and "False" if it is not the same.
    '''
    status = False
    if(len(obj)==intobj):
        status= True
    else:
        status = False
    return status

def range_check(obj1, obj2):
    '''
    It checks if "obj1" is in range of value of "obj2".
    It displays "True" if it is in range and "False" if it is not in range.
    '''
    status = False
    if(obj1>=obj2[0] and obj1<=obj2[1]):
        status= True
    else:
        status = False
    return status

def usage():
    '''
    It checks the usage of the script.
    It displays the usage status of the script.
    '''
    status = "Usage: a1_pbiswas1.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
    return status

if __name__ == "__main__":
    # step 1
    if len(sys.argv) != 2:
        print(usage())
        sys.exit()
    # step 2
    month_name = ['Jan','Feb','Mar','Apr','May','Jun',
         'Jul','Aug','Sep','Oct','Nov','Dec']
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
          7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    user_raw_data = sys.argv[1]
    # step 3
    allow_chars = '0123456789'
    dob = sanitize(user_raw_data, allow_chars)
    # setp 4
    result = size_check(dob,8)
    if result == False:
        print("Error 09: wrong date entered")
        sys.exit()
    # step 5
    year = int(dob[0:4])
    month = int(dob[4:6])
    day = int(dob[6:])
    # step 6
    result = range_check(year,(1900,9999))
    if result == False:
        print("Error 10: year out of range, must be 1900 or later")
        sys.exit()
    result = range_check(month,(1,12))
    if result == False:
        print("Error 02: wrong month entered")
        sys.exit()

    result = leap_year(year)
    if result == True:
        days_in_month[2] = 29

    result = range_check(day, (1, days_in_month[month]))
    if result == False:
        print("Error 03: wrong day entered")
        sys.exit()
    # step 7
    new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
    # step 8
    print(new_dob)
