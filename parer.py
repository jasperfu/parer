import csv
with open('batch63 raw.csv', newline='') as f:
    reader = csv.reader(f)
    with open('batch63Pared.csv', 'w', newline='') as w:
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
        morePrev = False
        prevPoint = False
        keep = False
        gap = False
        for row in reader:
            if p7 > max(p1, float(row[1]), p2, p3, p4, p5, p6,
                        p8, p9, p10, p11, p12, p13, p14, 1)
               and not morePrev:
                morePrev = prevPoint
                prevPoint = keep
                keep = True
                print("up")
            elif p7 < min(p1, float(row[1]), p2, p3, p4, p5, p6,
                          p8, p9, p10, p11, p12, p13, p14, -1)
                          and morePrev:
                morePrev = prevPoint
                prevPoint = keep
                keep = False
                print("down")
            if keep:
                writer.writerow(next(reader) + [batchId])
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

def hms_to_seconds(t):
    h, m, s = [int(i) for i in t.split(':')]
    return 3600*h + 60*m + s
