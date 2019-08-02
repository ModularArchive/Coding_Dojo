mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]

def id_list_type(First): #I attempted 1st but had to change to First due to computer not recognizing it
    new_string = ''
    total = 0

    for value in First:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is of string type"
        print "String", new_string

    else:
        print "The array you entered is of string type"
        print "Total:", total

print id_list_type(mixed_list)
print id_list_type(integer_list)
print id_list_type(string_list)
#I manually typed this in and adjusted according to what the solution was
#originally had each solution in a separate file but when I went to the 
#assignment solution I didn't notice the option to do so until afterwards