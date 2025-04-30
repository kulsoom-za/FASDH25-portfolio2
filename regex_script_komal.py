#importing regular expressions to find text patterns
import re
#importing os to enable interaction with the file system 
import os
#for handling tabular data and exporting tsv
import pandas as pd


#function that writes a list of data rows into a tsv file using pandas 
def write_tsv(rows, column_list, path):
   
    #convert the list of rows into pandas DataFrame
    df = pd.DataFrame(rows, columns=column_list)
    
    # write the dataframe to tsv:
    df.to_csv(path, sep="\t", index=False)



# Defining the folder where the articles are present
# these articles are text files to search for place names 
folder = "articles"  


#  define the path and load the gazetteer from the tsv file, having place names and alternate names 
path = "gazetteers/geonames_gaza_selection.tsv"
#open and read the file
with open(path, encoding="utf-8") as file:
    data = file.read()

# build a dictionary of patterns for each place name and a count of matches - Took help from ChatGPT (Conversation 1)
patterns = {}

#split the gazetteer data by a new line to et each row
rows = data.split("\n")

#skip the header as the pattern starts from the next row
for row in rows[1:]:
    columns = row.split("\t") # each column in tsv is separated by tabs 
    asciiname = columns[0] #first column has name for the place


    #Skip rows that don't have at least 6 columns and others may beb incomplete    
    if len(columns) < 6:
        continue

    #Initialize the list with the place name
    name_variants = [asciiname]


    # Get the alternate names from the 6th column which is counted as 5, if present
    alternate_names = columns[5].strip()

    
    if alternate_names:
        # Split the alternate names by comma and process each name
        alternate_list =alternate_names.split(",")
        for alternate in alternate_list:
            alternate = alternate.strip()
            if alternate:
                name_variants.append(alternate)

    #Building a single reger pattern that matches any variant (using '|' for alternation)
    regex_pattern = "|".join([re.escape(name) for name in name_variants])
    patterns[asciiname] = {"pattern": regex_pattern, "count":0}

    


# this dictionary stores how many times each place name was mentioned per month 
mentions_per_month = {}


#Set the starting date of the war in Gaza to filter articles - Help from ChatGPT - Conversation 2 and 4(removal of datetime)
war_start_date = "2023-10-07"

# Loop through each file to count the number of times each pattern is found in the entire folder:
for filename in os.listdir(folder):
    # Extract the date from the filename(as the format is YYYY-MM-DD_)
    date_str = filename.split("_")[0]

    #Skip the file if it is before the start of  the war
    if date_str < war_start_date:
        continue
    
    

# build the file path to the current articles:
    file_path = os.path.join(folder, filename)        

    #Open and read the articles 
    with open(file_path, encoding="utf-8") as file:
        text = file.read()
        

    # Loop through each place to search for matches in the text: - Help from ChatGPT - Conversation 3
    for place in patterns:
        pattern = patterns[place]["pattern"] # Get regex-safe pattern 
        matches = re.findall(pattern, text, re.IGNORECASE)
        count = len(matches) # number of times the place was found
        
        # add the number of times the place was found to the total frequency:
        patterns[place]["count"] += count
        
        # extract the month from the date string
        month_str = date_str[:7]
        

        # initialize place and month in mentions_per_month dictionary if not done already
        if place not in mentions_per_month:
            mentions_per_month[place] = {}
        if month_str not in mentions_per_month[place]:
            mentions_per_month[place][month_str] = 0

        #Add the new matches on the place names to the number of times it was mentioned that month     
        mentions_per_month[place][month_str] += count
          

# print the final dictionary showing how often each place was mentioned by month
# Loop through each place in the mentions_per-month dictionary
for place in mentions_per_month:
    # Start a dictionary like printout for the current place 
    print(f'"{place}": {{')

    #Get a list of all the months in which the place names are mentioned 
    month_list = list(mentions_per_month[place].keys())

    #loop through each month to print the corresponding mention count
    for month in month_list:
        count = mentions_per_month[place][month] #  get the count for that month

        # display the output with a comma except for the last item to keep it clean 
        if month != month_list[-1]:
            print(f'    "{month}": {count},')
        else:
            print(f'    "{month}": {count}')

    # close the dictionary block and print the output
    print("},")

#Convert the mentions_per_month dictionary to list of rows for output
rows = []

#loop through each place again to prepare structured data for export 
for place in mentions_per_month:

    # loop through each month and find the number of times the place is mentioned 
    for month in mentions_per_month[place]:
        count = mentions_per_month[place][month]

        #Append a tuple (place, month, count) to the rows list
        rows.append((place, month, count))

#Write final result to tsv file for external use        
write_tsv(rows, ["placename","month", "count"], "regex_counts.tsv")
