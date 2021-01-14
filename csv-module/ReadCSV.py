
import csv

with open('exchange.csv') as csvfile:
    data = csv.reader(csvfile, delimiter=',')

    # print the first 10 rows in the file
    for i, row in enumerate(data):
        print(row)
        if i >= 9:
            break


