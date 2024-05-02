"""
A chemistry teacher is very strict and wants the students do well in the class. to aid this, lectures on each
chapter will be repeated periodically through semester. In each class, the next chapter is presented.
When they reach end of the book the lecture start over with chapter 0. The first day of class is class[0] 
and first chapter is chapter 0. If there are 3 chapters , daily lectures on chapters 
class = [0, 1, 2, 0, 1, 2, ...]

one of the student is out of class for few days (begin day (b) and end day (e)).
find out the chapters the student will miss
"""

def missed_lectures(num_chapters, b, e):
    classes = []

    no_of_lectures = num_chapters * (e + 1)

    for i in range(no_of_lectures):
        classes.append(i % num_chapters)

    #print(classes)
    return set(classes[b-1 : e]), 

num_chapters = 4
b = 14
e = 16

print(missed_lectures(num_chapters, b, e))
