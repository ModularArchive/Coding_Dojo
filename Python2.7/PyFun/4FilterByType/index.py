sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
py_1 = lL

py_type = type(py_1)
if py_type is int:
    if py_1 >= 100:
        print "That's a big number"
    else:
        print "That's a small number"
elif py_type is str:
    if len(py_type) >= 50:
        print "Long sentence"
    else:
        print "Short sentence"
elif isinstance(py_1, list):
    if len(py_1) >= 10:
        print "Big list!"
    else:
        print "Short list"