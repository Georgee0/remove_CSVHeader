# remove_CSVHeader
At a high level, the program must do the following: 

1. Find all the CSV files in the current working directory. 
2. Read in the full contents of each file. 
3. Write out the contents, skipping the first line, to a new CSV file. 

At the code level, this means the program will need to do the following: 

1. Loop over a list of files from os.listdir(), skipping the non-CSV files. 
2. Create a CSV reader object and read in the contents of the file, using the line_num attribute to figure out which line to skip. 
3. Create a CSV writer object and write out the read-in data to the new file.
