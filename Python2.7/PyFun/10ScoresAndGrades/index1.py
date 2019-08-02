import random
def gradeScale():
    for i in range(10):
        score = random.randint(60,100)
        print score
        if score <= 70:
            print "Score:", score,"; Your grade is D"
        elif score <= 80:
            print "Score:", score,"; Your grade is C"
        elif score <= 90:
            print "Score:", score,"; Your grade is B"
        elif score <= 100:
            print "Score:", score,"; Your grade is A"

gradeScale()