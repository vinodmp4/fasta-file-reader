# Created by Vinod M P

inputfilename = 'test.fasta'                                    # Change the filename here.

output_dictionary = {}                                          # This is the output storing dictionary.

with open(inputfilename, 'r') as file:                          # Open the file
    current_header = ''                                         # At initialization, there is no header.
    for line in file:                                           # Looping through each line
        if line.startswith('>'):                                # Check whether it is a header line (start with '>' symbol).
            current_header = line[1:][:-1]                      # Save header name as current header.
            output_dictionary[current_header] = ""              # Initialized.
        else:
            if not(current_header == ''):                       # Just avoiding occurence of errors.
                if line.endswith('\n'):line = line[:-1]         # pre-processing sequence if it contain unwanted newline character.
            output_dictionary[current_header] += line           # append the sequence to value of its header key.
headers = list(output_dictionary.keys())                        # Collecting all header names into a list/array

for header in headers:                                          # looping through all headers
    print(header)                                               # print header
    print(output_dictionary[header])                            # print sequence
