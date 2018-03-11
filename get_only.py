# File A content
file_a = '/Users/carol/Desktop/bst.txt'
with open(file_a) as filea:
    a_data = [a.strip() for a in filea]

# File B content
file_b = '/Users/Carol/Desktop/scripts/GTEX/GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_rpkm.txt'
with open(file_b) as fileb:
    b_data = [[l.strip() for l in line.split()] for line in fileb]

# Get target columns indexes
# Include: 'field' and 'id' index
# while loop nested in for loop to ignore ValueError
indexes = [0, 1]
for a in a_data:
     indexes.append(b_data[0].index(a))

print(indexes.append(b_data[0].index(a)))

# Filter data
new_data = []
for line in b_data:
    new_line = []

    for index in indexes:
        new_line.append(line[index])

    new_data.append(new_line)

# Separate columns by tabs/rows by line breaks
new_data_string = '\n'.join(['\t'.join(line) for line in new_data])

# Save merged data
# print(new_data_string)

new_file = '/Users/Carol/Desktop/new.txt'
f = open(new_file, 'w')
f.write(new_data_string)

f.close()

