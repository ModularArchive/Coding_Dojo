#Assignment 2
string = "It's thanksgiving day. It's my birthday,too!"
print string
print string.find("day")
string = string.replace("day", "month")
print string

#part 2
x = [-10,2,3,9,37]
print x
print min(x)
print max(x)

#part 3
x = ["Heya","Howdy","Howsitgoin",1,2,3]
print x[0], x[len(x) - 1]

#print4
x= [12,3,4,6,7,8,9,10]
print x.sort()
print x
first_list = x[:len(x)/2]
second_list = x[:len(x)/2]
print "first_list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
