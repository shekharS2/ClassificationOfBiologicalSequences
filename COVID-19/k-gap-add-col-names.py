import numpy as np
import pandas as pd
import csv

with open('k-gap-63.csv','w', newline = '') as newFile:
    newFileWriter = csv.writer(newFile)
    row = []
    row.append("Sequence")
    row.append("SequenceID")
    for a in range(4):
        if a == 0:
            char1 = 'a'
        elif a == 1:
            char1 = 'c'
        elif a == 2:
            char1 = 'g'
        else:
            char1 = 't'
            
        for b in range(4):
            if b == 0:
                char2 = 'a'
            elif b == 1:
                char2 = 'c'
            elif b == 2:
                char2 = 'g'
            else:
                char2 = 't'
            for k in range(64):
                colName = char1 + char2 + " " + str(k)
                row.append(colName)
    #print(row)
    newFileWriter.writerow(row)
