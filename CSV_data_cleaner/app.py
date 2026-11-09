import csv

with open('sample.csv', mode='r') as infile, open('clean_data.csv', mode='w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        cleande_row = [cell.strip() for cell in row]

        writer.writerow(cleande_row)

print("CSV file cleaned")