texp = {}
with open("tex_parse_result.txt", "r") as f:
    for line in f:
        line = line.split(" ")
        texp[line[0]] = int(line[1][0])
# print(texp)
pdfp = {}
with open("number_results.txt", "r") as f:
    for line in f:
        pdfp[line[2:11]] = int(line[-3])
# print(pdfp)
total = 0
match = 0
for i in texp:
    if(i in pdfp):
        total += 1
        match += int(texp[i] == pdfp[i])
print(match*100/total)