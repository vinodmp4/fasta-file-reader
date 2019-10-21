# Created by Vinod M P
# Useful while using blast2go like softwares


outputheader = """
----------------------------------------------------------------
                        FASTA STATISTICS
----------------------------------------------------------------
"""

filename = input("Enter the Fasta filename:")			# Ask user to input name of the analysing fasta file

cmd = ["Started reading",
       "Finished reading",
       "Filename:\t\t",
       "Total basepairs:\t",
       "Total sequence:\t\t",
       "Mean:\t\t\t",
       "\n","-"*64,
       "Maximum sequence length:",
       "Minimum sequence length:"]						# Output associated texts - organised in a list

fasta = []												# Array to store data
print(cmd[0],filename)									# Declaring start of reading file
with open(filename,'r') as file:						# The process similar to read_fasta.py
    current_sequence = ""
    for line in file:
        if line.startswith('>'):
            if not(current_sequence==""):fasta.append(len(current_sequence))
            current_sequence = ""
        else:
            if line.endswith('\n'):line = line[:-1]
            current_sequence += line
    if not(current_sequence==""):fasta.append(len(current_sequence))
print(cmd[1],filename)									# Declaring end of reading file
total_bp = sum(fasta)									# sum of base pairs in file
total_seq = len(fasta)									# total number of sequence equal to total item in list
max_seq_length = max(fasta)								# maximum number of  basepair found in a single sequence
min_seq_length = min(fasta)								# minimum number of basepair found
mean = total_bp/total_seq								# mean value : average basepair per sequence
print(outputheader)										# start of printing output
print(cmd[2],filename)
print(cmd[3],total_bp)
print(cmd[4],total_seq)
print(cmd[5],mean,cmd[6])
print(cmd[7])
print(cmd[8],max_seq_length)
print(cmd[9],min_seq_length)
print(cmd[7])
