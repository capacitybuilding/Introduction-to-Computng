phone = {'mark': '095541...', 'bob': '091155...', 'john': '097788...', 'clark': '093366...'}


phone['john'] = '090000...'
print phone
print len(phone)

phone['harry'] = '099999***'
print phone
print len(phone)

del phone['bob']
print phone

x = phone.keys()
y = phone.values()
z = phone.items()
print x
print y
print z

print phone.has_key('bob')
phone.pop('harry')
print phone


for i in phone:
    print i
    
for i in phone:
    print phone[i]

print 'mark' in phone
print '095541...' in phone
