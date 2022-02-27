# python3
# removeCsvHeader.py : Remove header from all Csv file


import csv, os
os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for CsvFilename in os.listdir('.'):
    if not CsvFilename.endswith('.csv'):
        continue    # skip non csv files
    print('Removing header from ' + CsvFilename + '........')
    
    # Read the csv files in without the header
    csvRows = []
    csvFileObj = open(CsvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
       # csvFileObj.close()
    
    # Write out the CSV files     
    csvFileObj = open(os.path.join('headerRemoved', CsvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
print('Task Done!')        