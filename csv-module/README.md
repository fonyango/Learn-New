# Using csv module to read and write files

Reading a csv file in python using a csv module is pretty easy. The process is as follows:

- Begin by importing the csv library.
- Use open() function to open the csv file as a file object. The open() function is a python in-built function.
- Use csv reader to convert the file object to a csv.reader object.
- Create a for loop to loop through the rows and store data.
- Print the rows. You can specify the number of rows you want to print by using an if statement.

Feel free to check my article on my personal blog: https://yourdataguy.org/how-to-read-a-csv-file-in-python-using-csv-module/


To write a csv file, follow the steps below:

- Start by importing csv library
- Create a list of lists named rows to contain the rows of your data records.
- Use open() function to open the csv file in WRITE mode as a csv file.
- Convert the file object to a csv.writer object using a csv.writer function.
- Lastly, use writer.writerow() to write the fields and rows.

You can also check my website for the article on how to write a csv file: https://yourdataguy.org/how-to-write-a-csv-file-in-python-using-csv-module/
