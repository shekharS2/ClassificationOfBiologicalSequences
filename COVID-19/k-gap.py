import numpy as np
import pandas as pd
import csv

dataset = pd.read_csv("combined-db.csv")
#print(len(dataset))

datasetSeq = dataset.Sequence
#print(datasetSeq[0])
SeqID = dataset.SequenceID

with open('combined-k-gap.csv','w', newline = '') as newFile:
    newFileWriter = csv.writer(newFile)
    for x in range (len(dataset)):
        seq = datasetSeq[x]
        seqRow = []
        seqRow.append(seq)
        seqRow.append(SeqID[x])
        
        for a in range(4):
            if a == 0:
                char1 = 'A'
            elif a == 1:
                char1 = 'C'
            elif a == 2:
                char1 = 'G'
            else:
                char1 = 'T'
                
            for b in range(4):
                if b == 0:
                    char2 = 'A'
                elif b == 1:
                    char2 = 'C'
                elif b == 2:
                    char2 = 'G'
                else:
                    char2 = 'T'
                
                for k in range(64):
                    count = 0
                    for i in range(len(seq) - (k + 1)):
                        if seq[i] == char1 and seq[i + (k + 1)] == char2:
                            count = count + 1
                            
                    countRatio = count/(len(seq) - (k + 1))
                    seqRow.append(countRatio)
                    #col_name = char1 + char2+ " " + str(k)
                    #print(col_name, end = ": ")
                    #print(countRatio)
                    #dataset.set_value(i, col_name, countRatio)
                    #dataset.to_csv('k-gap.csv', index=False)
        #print(seqRow)
        newFileWriter.writerow(seqRow)
        

