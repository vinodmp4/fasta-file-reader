# fasta-file-reader
This python program will read fasta file and store it in a dictionary.

# ---------------------------------------------------------------
FASTA files are text-based format for storing nucleotide / peptide sequences.
Inside the file, each sequence begins with a single line description. The description
line starts with a greater than ('>') symbol. Description is followed by lines 
containing sequence data.

Example:

    >M37817.1 Human keratin psi-K#16-1 pseudogene, 3'end
    GAGATGCTTGCTCTGCGAGGTCAGACCGGTGGAGAAGTGAACGTGGAGACGGATGCCGCACCTGGCGTGG
    ACCTGAGCTGCATCCTGAATGAGATGCGCAACCAGTACGAGCAGATGGCAAAGCACAACCACAGAGATGC
    TGGGCCTGTGGTTCCTGAGCAAGACCAAGGAGCTGAACAAAAAAGTGGCCTCCAGCAGTGAACTGGTACA
    GAGCAGCAGCTGCAGTGAGGTGACGGAGCTCCAGAGGGTGTTCCAGGGCCTGGAGATGGAGCTGCAGTCC
    CAGCTCAGCATANNNNNGATCCAGGGACTGATTGGCAGTGTGGAGGAGCAGCTGGCCCAGCTATGCTGTG
    AGATGGAGCAGCAGAGCCGGGAGTACCAGATCTTGCTGGACATGAAGACACGGCTGGAGCAGGAGATCGC
    

In this python program, the specified file is opened and processed to store individual 
sequence data into a dictionary.
