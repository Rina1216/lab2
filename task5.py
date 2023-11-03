from csv import reader
list1 = []
list2 = []

output = open('result.txt', 'w')
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        list1.append(row)
    list1 = list1[1:]
    for row in list1:
        if row[4] not in list2:
            list2.append(row[4])
            print(row[4])