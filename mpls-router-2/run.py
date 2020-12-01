#!/bin/python3

# Olivier Bonaventure, 2020

from inginious import input, feedback
import re
 
def removeSpaces(string):
    return re.sub('[\s+]', '', string)

def getStack(string):
    return (removeSpaces(string.upper()))

def checkStack(q,correct):
    stack=getStack(input.get_input(q))
    response = ""
    errors = 0
    grade = 0
    if(stack == correct):
        grade=100
        feedback.set_problem_result("success", q)
        feedback.set_problem_feedback(response, q)
        return grade
    else:
        if not (stack.startswith( correct[0:1] ) ):
            response += "The top-label of your stack is incorrect.\n"

        if not (stack.endswith( correct[-2:] ) ):
            response += "The bottom label of your stack is incorrect.\n"

        clist=correct.split(':')
        slist=stack.split(':')
        if len(slist) > len(clist):
            response += "Your answer contains more labels in its stack than the correct one.\n"
        if len(slist) < len(clist):
            response += "Your answer contains fewer labels in its stack than the correct one.\n"
            
        feedback.set_problem_result("failed", q)
        response += "Your answer to this question is incorrect.\n"
        feedback.set_problem_feedback(response, q)
        return grade


        
grade=0
grade += checkStack("q1","L3:L4:L2")/5
grade += checkStack("q2","L7:L4:L1")/5
grade += checkStack("q3","L9:L1")/5
grade += checkStack("q4","L0:L5")/5
grade += checkStack("q5","L1:L9:L3")/5



feedback.set_grade(grade)

if grade >= 99:
    feedback.set_global_result("success")
else:
    feedback.set_global_result("failed")
# end

