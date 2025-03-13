# creating a variable and storing the text
import csv
with open('P0-P2.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        print(row['Name'])

        FileName = "P2 Extract - "+row['Name']

        # text that we want to add 
        P0_1_Code = str(row['p01'])
        P0_2_Code = str(row['p02'])
        P1_1_Code = str(row['p11'])
        P1_2_Code = str(row['p12'])
        P2_Code = str(row['p2'])

          
        # Opening our text file in read only 
        # mode using the open() function 
        with open('P0-P2.json', 'r') as file: 
          
            # Reading the content of the file 
            # using the read() function and storing 
            # them in a new variable 
            data = file.read() 
          
            # Searching and replacing the text 
            # using the replace() function
            
            data = data.replace("P0-1", P0_1_Code)
            data = data.replace("P1-1", P1_1_Code)
            data = data.replace("P0-2", P0_2_Code)
            data = data.replace("P1-2", P1_2_Code)
            data = data.replace("P2", P2_Code)
            data = data.replace(" ", "").replace('\n', '').replace('\r', '')
            data = data.replace("Title", FileName)
          
        # Opening our text file in write only 
        # mode to write the replaced content 
        with open(FileName+".json", 'w') as file: 
          
            # Writing the replaced data in our 
            # text file 
            file.write(data) 
          
        # Printing Text replaced 
        print("Text replaced") 
