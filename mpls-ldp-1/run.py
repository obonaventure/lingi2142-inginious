#!/bin/python3

# Olivier Bonaventure, 2019

from inginious import input, feedback
import re
 
def removeSpaces(string):
    return re.sub('[\s+]', '', string)

def toList(string):
    return (removeSpaces(string.upper())).split(',')


def getPath(string):
    return (removeSpaces(string.upper()))



def checkSinglePath(q,correct):
    path=getPath(input.get_input(q))
    response = ""
    errors = 0
    grade = 0
    if(path == correct):
        grade=100
        feedback.set_problem_result("success", q)
        feedback.set_problem_feedback(response, q)
        return grade
    else:
        if not (path.startswith( correct[0:1] ) ):
            response += "Your answer does not start with {}\n".format(correct[0:1])

        if not (path.endswith( correct[-2:] ) ):
            response += "Your answer does not end with {}\n".format(correct[-2:])
        if (',' in path):
            response += "There is only one path from this router.\n"
            
        feedback.set_problem_result("failed", q)
        response += "Your answer to this question is incorrect. There is only one path from this router to the destination.\n"
        feedback.set_problem_feedback(response, q)
        return grade

def checkNPaths(q,correct):
    path=getPath(input.get_input(q))
    list=path.split(',')
    clist=correct.split(',')
    errors = 0
    grade = 0
    response = ""

    if(len(list) != len(clist) ):
        feedback.set_problem_result("failed", q)
        response += "Your answer to this question is incorrect. There are {} equal cost paths from this router.\n".format(len(clist))
        feedback.set_problem_feedback(response, q)
        return 0
    
    for l in clist:
        if not(l in list):
            feedback.set_problem_result("failed", q)
            response += "Your answer to this question is incorrect.\n"
            feedback.set_problem_feedback(response, q)
            return 0

    feedback.set_problem_result("success", q)
    feedback.set_problem_feedback(response, "q1")
    return 100


        
grade=0
grade += checkNPaths("r1","R1-R3,R1-R6-R5")/2
grade += checkSinglePath("r6","R6-R5")/2



feedback.set_grade(grade)

if grade >= 99:
    feedback.set_global_result("success")
else:
    feedback.set_global_result("failed")
# end

