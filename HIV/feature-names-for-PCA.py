import numpy as np
import pandas as pd
import csv

with open('k-gapXXX.csv','w', newline = '') as newFile:
    newFileWriter = csv.writer(newFile)
    row = []
    for i in range(1,701):
        col = "'principal component" + str(i) + "'"
        row.append(col)
    print(row)
    newFileWriter.writerow(row)
