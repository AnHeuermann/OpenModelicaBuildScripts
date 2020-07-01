from fmpy import *
import os
import sys

# first argument is the path to the FMU
filename = sys.argv[1]

# save the CVS next to the FMU
csv_file, _ = os.path.splitext(filename)
csv_file += '_out.csv'

model_description = read_model_description(filename)

output = []

# collect the variables to log
for variable in model_description.modelVariables:
    if variable.causality in {'input', 'output', 'local'}:
        output.append(variable.name)

# simulate the FMU
result = simulate_fmu(filename, output=output)

# write the CSV
write_csv(csv_file, result)