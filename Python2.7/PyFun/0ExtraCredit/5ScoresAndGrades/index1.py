import random
def grade():
    for i in range(10):
        score = random.randint(60,100)
        print score
        if score <= 60:
            grade = "D"
        elif score <= 70:
            grade = "C"
        elif score <= 80:
            grade = "B"
        elif score <= 90:
            grade = "A"
        print "Your score is {}, Your grade is a {}".format(score,grade)
grade()