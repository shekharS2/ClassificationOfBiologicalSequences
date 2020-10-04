#2 remove '>'

filename = 'output.txt'
stripped_line = ''

f = open("pvivaxtemp.csv", "w")
with open(filename, 'r') as fh:
    for line in fh:
        #line = line[:15] + "," + line[15:]
        line = line.replace('>','')
        f.write(line)
fh.close()
f.close()
