old_file = open('city.txt', 'r')
new_file = open('city_with_format.txt', 'w')
all_cities = old_file.readlines()
# print all_cities
for i in all_cities:
    city, country = i.strip().split()
    new_file.write('%-25s%-25s\n' % (city, country))

old_file.close()
new_file.close()
