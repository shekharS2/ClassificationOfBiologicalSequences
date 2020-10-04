import numpy as np
import pandas as pd
import csv

dataset = pd.read_csv("pvivaxtemp.csv")
#print(len(dataset))

datasetSeq = dataset.Sequence
#print(datasetSeq[0])
SeqID = dataset.SequenceID


with open('pvivax.csv','w', newline = '') as newFile:
    newFileWriter = csv.writer(newFile)
    for x in range (len(dataset)):
        seq = datasetSeq[x].upper()
        seqRow = []
        seqRow.append(seq)
        seqRow.append(SeqID[x])
        #print(seqRow)
        newFileWriter.writerow(seqRow)
        
        
        