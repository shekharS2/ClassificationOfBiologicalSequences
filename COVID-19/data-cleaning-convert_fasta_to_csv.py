#1 removes newline character
#This creates a new string based on the > character and combines the string until the next >. It then appends to a running list.

# open file and iterate through the lines, composing each single line as we go
out_lines = []
temp_line = ''
with open('pvivax.fasta','r') as fp:
    for line in fp:
        if line.startswith('>'):
            out_lines.append(temp_line + '\n')
            temp_line = ''
            line = line.replace(' ', '')
            line = line.replace(',', '-')
            temp_line = line.strip() + ","
        else:
            line = line.replace('-', '')
            temp_line += line.strip()
        
    #print(out_lines)
    
with open('output.txt', 'w') as fp_out:
    for line in out_lines:        
        fp_out.write(line)
fp_out.close()