# Filter a given csv file for a list of variables and save filtered csv file.

import sys
import pandas

delimiter=','

# Show help
if len(sys.argv) <= 3:
    print("filterCSV.py\n\tFilter a given csv file for a list of variables and save filtered csv file.")
    print("Usage: \n\t$ python filterCSV.py \'inFile.csv\' \'outFile.csv\' \'var1\' [\'var2\' ...]")
    print("Example call: \n\t$ python filterCSV.py 'BouncingBall_ref.csv' 'BouncingBall_ref_filtered.csv' 'v' 'h' 'der(v)' 'der(h)'")
    exit(0)

# first argument is name of input csv file
csv_filename_in = sys.argv[1]
print("Reading input file: ", csv_filename_in)

# second argument is name of output csv file
csv_filename_out = sys.argv[2]
print("Writing to output file: ", csv_filename_out)

# Other arguments are variable names to filter
variables=['time']
for arg in sys.argv[3:]:
    variables.append(arg)

print("Filtering for variables: ", variables)
filtered_df = pandas.read_csv(csv_filename_in, usecols=variables)

# Write output file
filtered_df.to_csv(csv_filename_out, index = False)