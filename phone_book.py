import csv
# open the CSV file safely and close it automatically when done
with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
# iterate over each row (as a dictionary) in the CSV
    for row in csv_reader:
        last_name = row["last_name"]      # use column name
        phone_number = row["phone_number"]      # use column name
        print(f"{last_name}: {phone_number}")
