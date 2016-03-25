import json


res = {}
with open("stat.json") as fp:
    res = json.load(fp)
kt = list(res.keys())
km = {}
kl = []
for key in kt:
    ym = key.split("-")
    ym = ym[0] + "-" + ym[1].zfill(2)
    kl.append(ym)
    km[ym] = key

kl.sort()

with open("out.csv", "w") as fp:
    fp.write("yearmonth,pos,neg,neutral\n")
    for k in kl:
        key = km[k]
        fp.write(k + "," + str(res[key]["pos"]) + "," + str(res[key]["neg"]) + "," + str(res[key]["neutral"]) + "\n")
