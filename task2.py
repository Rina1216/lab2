from csv import reader
name = input('search for?')
flag = 0
list1 = []
with open('books-en.csv') as file:
    table = reader(file, delimiter=';')
    for row in table:
        list1.append(row)
    list1 = list1[1:]
    for row in list1:
        lower_case=row[2].lower()
        index = lower_case.find(name.lower())
        cost = row[-1]
        if ',' in cost:
            cost = cost.replace(',','.')
        if index!=-1 and float(cost)<=150:
            print (f'{row[0]}. {row[2]}. Цена {cost} рублей.\n')
            flag = 1
        elif index!=-1 and float(cost)>150:
            print(f'{row[0]}. {row[2]}. Цена {cost} рублей.\n', 'sorry, you have not enough many')
            flag = 1
    if flag == 0:
        print ('Nothing found.')