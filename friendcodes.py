import csv

# Load friendcodes
fc = []
with open("res/fcdb.csv", "rb") as f:
    fcreader = csv.reader(f)
    for row in fcreader:
        fc.append(row)
    f.close()

def friendcodes():
    ret = ""
    for i in range(0, len(fc), 2):
        ret += fc[i][0] + ": " + fc[i+1][0] + "\n"
    return ret
