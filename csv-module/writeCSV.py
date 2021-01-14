import csv

# create a list of lists for rows of the file

rows = [['name', 'age', 'department', 'salary'],
        ['Ray', '29', 'accounting', '568'],
        ['Caleb', '31', 'human resource', '610'],
        ['Kendrick', '28', 'production', '605'],
        ['Christina', '30', 'Sales', '590']]

# open as csvfile
with open('staff_file.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    # write rows of the file
    csv_writer.writerows(rows)

    