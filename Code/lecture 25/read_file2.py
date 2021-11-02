stud = open("student.txt", "r")
s_id = stud.readlines()
print s_id
for i in s_id:
    print i.strip().split()
