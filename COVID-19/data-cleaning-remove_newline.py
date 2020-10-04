filename = 'corona-full.fasta'
stripped_line = ''

f = open("output.txt", "a")

with open(filename, 'r') as fh:
    for line in fh:
        if '>' in line:
            stripped_line = stripped_line + "\n"
            f.write(stripped_line)
            stripped_line = ''
            stripped_line = stripped_line + line.rstrip("\n") + ","
        else:
            stripped_line = stripped_line + line.rstrip("\n")
stripped_line = stripped_line + "\n"
f.write(stripped_line)
fh.close()
f.close()