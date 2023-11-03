from csv import reader
list1 = []
import random

output = open('result.txt', 'w')
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        list1.append(row)
    list1 = list1[1:]
    for i in range(20):
        c = random.randint(0,len(list1))
        row = list1[c]
        output.write(f'{i+1}. {row[2]}. {row[1]} - {row[3]} ')



output.close()





