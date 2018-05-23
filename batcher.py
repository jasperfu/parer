import csv
import time
import datetime

with open('betterHMSweirdepoch.csv', newline='') as f:
    reader = csv.reader(f)
    with open('batchedFirstTry.csv', 'w', newline='') as w:
        writer = csv.writer(w)
        writer.writerow(next(reader))
        batchId = 0
        for row in reader:
            if batchId == 0:
                writer.writerow(row)
                batchId += 1
            elif float(row[4]) != batchId:
                writer.writerow(p)
                writer.writerow(row)
            p = row
