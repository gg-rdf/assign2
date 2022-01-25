import csv
from csv import reader, writer

file_list = []

with open('wk2_test1_in.csv', 'r', encoding='UTF8') as csv_file:
    reader = csv.reader(csv_file,delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)

    for row in reader: # for each line in file
        temp_list = []
        for column in row: # for each record
            value = column.split() # split record in spaces
            for v in value:
                if len(v) <10: # add spaces if word is smaller than 10 chars
                    v = v + (" " * (10 - len(v)))
                elif len(v) > 15: # truncate if word is longest than 15 chars
                    v = v[:15]
                temp_list.append(v) # add values to temp list
        if temp_list: # if temp list created
            file_list.append(temp_list)  # add it to final list

with open('wk2_test1_out.csv', 'w', encoding='UTF8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar="'",quoting=csv.QUOTE_MINIMAL)

    writer.writerows(file_list) # store list to new csv
