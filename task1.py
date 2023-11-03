from csv import reader
resoult = 0
with open('books-en.csv') as file:
    table = reader(file, delimiter=';')
    for row in table:
        if len(row[1])>30:
            resoult+=1
print(resoult)