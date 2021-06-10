import csv

f = open('output.csv', 'w', newline='')
wr = csv.writer(f)
f2 = open('input.csv', 'r')
rdr = csv.reader(f2)
for line in rdr:
	if line: wr.writerow(line)
f.close()