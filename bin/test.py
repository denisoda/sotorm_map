import csv

csv_file_path = 'data/csv/Storm.csv'

with open(csv_file_path) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['YEAR'])





