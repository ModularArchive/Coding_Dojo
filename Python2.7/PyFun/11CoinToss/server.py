import random

def toss(reps): #toss calls on the reps int in range(1, reps)
    attempt_count = 1
    head_count = 0
    tail_count = 0
    result = ""
    result_string_complete = ""

    for i in range(1, reps):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            head_count += 1
            result = "head"
            print "Attempt #", attempt_count, ":Throwing a coin... its a", result, "! Got", head_count, "head(s) so far and", tail_count, "tail(s) so far"
        else:
            tail_count += 1
            result = "tail"
            print "Attempt #", attempt_count, ":Throwing a coin... its a", result, "! Got", head_count, "head(s) so far and", tail_count, "tail(s) so far"
        attempt_count += 1

toss(5001) #Value of # of reps to be used