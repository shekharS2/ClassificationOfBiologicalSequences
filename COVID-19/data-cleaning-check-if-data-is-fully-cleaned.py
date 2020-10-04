filename = 'input.txt'
stripped_line = ''

#=====================================================================================================

#remove left out '>' chars

count = 0
with open(filename, 'r') as fh:
    for line in fh:
        count = count + 1
        if '>' in line:
            print("'>' found in line no:", end = " ")
            print(count)
            break
fh.close()

#=======================================================================================================

#check for duplicate entries

lines_seen = set()  # holds lines already seen

infile = open('input.txt', "r")
outfile = open('output.txt', "w")
count = 0

#print("The file bar.txt is as follows")
for line in infile:
    #print(line)
    count = count + 1
    if line in lines_seen:
        print("Duplicate line at line no.: ")
        print(count)
        continue
    lines_seen.add(line)
    #if line not in lines_seen:  # not a duplicate
        #outfile.write(line)
        #lines_seen.add(line)
outfile.close()

#========================================================================================================

#copy txt file contents to csv file

ifile = "input.txt"
f = open('corona-db-main.csv', "w")

with open(ifile, "r") as fp:
    for line in fp:
        f.write(line)
f.close()
        
#========================================================================================================

#small letters to capital letters



