# Python 3
# Program to read Fasta File and calculate Contig Length for creating graphs
import sys
try:
    filename = sys.argv[1]
    if len(sys.argv)>2:print("Only first argument as input file is accepted.")
except:
    print("Usage [Linux]: python3 contig_length input_file.fasta\nUsage [Windows]: python contig_length input_file.fasta")
    sys.exit(1)
hdr = ["<_100nt","100-500","501-1000","1001-1500","1501-2000","2001-2500","2501-3000",">3000nt"]
contig_data = {hdr[0]:0,hdr[1]:0,hdr[2]:0,hdr[3]:0,hdr[4]:0,hdr[5]:0,hdr[6]:0,hdr[7]:0}
try:
    with open(filename,'r') as file:
        for line in file:
            if not(line.startswith(">")):
                cont_len = len(line.rstrip())
                if cont_len > 3000:contig_data[hdr[7]]+=1
                elif cont_len > 2500:contig_data[hdr[6]]+=1
                elif cont_len > 2000:contig_data[hdr[5]]+=1
                elif cont_len > 1500:contig_data[hdr[4]]+=1
                elif cont_len > 1000:contig_data[hdr[3]]+=1
                elif cont_len > 500:contig_data[hdr[2]]+=1
                elif cont_len > 100:contig_data[hdr[1]]+=1
                elif cont_len < 100:contig_data[hdr[0]]+=1
                else:pass
except:
    print("Error Reading File")
    sys.exit(1)
try:
    print(filename)
    for n in hdr:
        print(n,"\t",contig_data[n])
except:
    print("Error While Printing Values")
    sys.exit(1)
