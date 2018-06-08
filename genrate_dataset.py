import io
"""
change data set from test to csv in this web site http://www.dcs.bbk.ac.uk/~ROGER/corpora.html
"""
with open("missp.dat.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

file = io.open("out_csv.csv", mode="w",encoding='utf-8')
notdol=" "
for contents in content:

    if contents.startswith("$"):
        hasdol=contents
    else:

        notdol=contents
        row = hasdol + ',' + notdol + '\n'
        file.write(row)
        print(row)
