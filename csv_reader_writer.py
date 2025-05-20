import csv

# Define a function to extract the sort key
def get_second_col(row):
    return int(row[1])

# Read the CSV file
with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Separate header and data
header = rows[0]
data_rows = rows[1:]

# Sort the data by the second column
sorted_rows = [header] + sorted(data_rows, key=get_second_col)

# Write the sorted data to a new file
with open('sorted_sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sorted_rows)
