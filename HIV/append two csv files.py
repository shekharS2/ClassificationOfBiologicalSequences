import csv
reader = csv.reader(open("k-gap.csv"))
reader1 = csv.reader(open("combined.csv"))
f = open("k-gap1.csv", "a", newline = '')
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)
f.close()