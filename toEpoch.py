import csv
import time
import datetime

def epoch(t):
    pattern = '%Y-%m-%d %H:%M:%S.%f'
    epoch = datetime.datetime.strptime(t, pattern)
    return (epoch.timestamp())

with open('dataload03262018.csv', newline='') as f:
    reader = csv.reader(f)
    with open('betterHMSonlyEpoch.csv', 'w', newline='') as w:
        writer = csv.writer(w)
        writer.writerow(next(reader))
        for row in reader:
            writer.writerow(row[:4] + [epoch(row[4])])
