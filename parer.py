import csv
import time
import datetime

def epoch(t):
    pattern = '%Y-%m-%d %H:%M:%S.%f'
    epoch = datetime.datetime.strptime(t, pattern)
    return (epoch.timestamp())

with open('dataload03262018.csv', newline='') as f:
    reader = csv.reader(f)
    with open('betterHMSweirdepoch.csv', 'w', newline='') as w:
        writer = csv.writer(w)
        writer.writerow(next(reader))
        batchId = 0
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        p6 = 0
        p7 = 0
        p8 = 0
        p9 = 0
        p10 = 0
        p11 = 0
        p12 = 0
        p13 = 0
        p14 = 0
        prevPoint = True
        keep = False
        gap = False
        counter = 0
        for row in reader:
            if (p7 > max(p1, float(row[1]), p2, p3, p4, p5, p6, p8, p9, p10, p11, p12, p13, p14, 1)) and not prevPoint:
                prevPoint = keep
                keep = True
                print("up:")
                print(p7)
            elif (p7 < min(p1, float(row[1]), p2, p3, p4, p5, p6, p8, p9, p10, p11, p12, p13, p14, -1)) and prevPoint:
                prevPoint = keep
                keep = False
                print("down:")
                print(p7)
            if keep:
                writer.writerow(row[:4] + [epoch(row[4])]  + [batchId])
                gap = False
            elif gap == False:
                batchId += 1
                gap = True
            p14 = p13
            p13 = p12
            p12 = p11
            p11 = p10
            p10 = p9
            p9 = p8
            p8 = p7
            p7 = p6
            p6 = p5
            p5 = p4
            p4 = p3
            p3 = p2
            p2 = p1
            p1 = float(row[1])
