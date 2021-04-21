import csv

# opening and reading CSV file
try:
    with open('names.csv', 'r') as f:
        csv_read = csv.reader(f)
        for i in csv_read:
            # print(i)
            continue


except Exception as e:
    print(e)

# opening and writing one csv to another
try:
    with open('names.csv', 'r') as f:
        csv_read = csv.reader(f)
        with open('names1.csv', 'w') as CsvToWrite:
            csv_write = csv.writer(CsvToWrite, delimiter='-')
            for i in csv_read:
                csv_write.writerow(i)


except Exception as e:
    print(e)

