seq = "A6.txt";
seqNew = "formatted-A6.csv";
fr = open(seq, 'r');
fw = open(seqNew, 'w');
for i in range(1501):
    line = fr.readline();
    if '\t' in line:
        line = line.replace("\t",",");
    fw.write(line);
    print(line);

fw.close();
fr.close();

##############################################################################################
#file_content = fr.read();
#print(file_content)

#line = fr.readline();
#cnt = 1;
#if line:
#    while line:
#        print("Line {}: {}".format(cnt, line.strip()));
#        line = fr.readline();
#        cnt += 1;
#else:
#    print("ERROR!");

#for line in fr:
#    print(line);
#fr.close();

#################################################################################################
#line = fh.readline();

#meta = ''
#sequence = ''
#while line:
#    line = line.rstrip('\n');
#    if '>' in line:
#        meta = line;
#    else:
#        sequence = sequence + line;
#    line = fh.readline();
#print(meta);
#print(sequence);

#import re
#seqobj = re.search()