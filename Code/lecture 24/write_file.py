stud = open("student.txt", 'w')
for i in range(3):
    s_id = raw_input('Enter id: ')
    stud.write(s_id + '\n')
stud.close()
