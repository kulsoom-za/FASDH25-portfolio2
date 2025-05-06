# FASDH25-portfolio2 

A repository for students' portfolios for mini-project 2 

 

# Mini Project 2: Visualizing Place Names in News Articles 

The mini project two requires us to extract and visualize place names and alternate names which were spelled differently in the news articles on Al Jazeera about the war in Gaza with the help of two methods: gazetteer and regular expressions and Named Entity Recognition. The goal is to extract and visualize the names over time and then compare the results of both the methods and the maps generated from regex and NER. We also have to describe the advantages and disadvantages of both the techniques. 

The first task before coding was to create an independent copy of our portfolio repository from git hub, which had to be created by a single member and the rest of us cloned that to our computers through Git Bash. 

  

## Repository Structure  

FASDH25-portfolio2/ 
├── articles/                  # Raw news articles (YYYY-MM-DD_ID.txt) 
├── Scripts/ 
│   ├── regex_script_final.py  # Gazetteer+Regex extraction 
│   ├── Gaza_NER2_KMK.ipynb    # NER extraction 
│   ├── build_gazetteer.py     # Geocoding script 
│   ├── NER_map.py            # NER visualization 
│   ├── Regex_map.py          # Regex visualization 
│   ├── ner_counts.tsv        # NER output 
│   └── regex_counts.tsv      # Regex output 
├── gazetteers/ 
│   ├── geonames_gaza_selection.tsv  # Primary location data 
│   ├── countries.tsv         # Country references 
│   ├── NER_gazetteer.tsv     # Auto-geocoded results 
│   └── README 
├── Maps/ 
│   ├── NER_map.html          # Interactive NER map 
│   ├── NER_map.png           # NER static map 
│   ├── regex_map.html        # Interactive regex map 
│   └── regex_map.png         # Regex static map 
├── AI_Documentation/         # Team reports 
    ├── Al_Documentation_komal_ali.docx 
    ├── Al_documentation_kulsoom_zaman.docx 
    └── Al_documentation_Mahpara_karim.docx 

├── .gitignore 

├── frequencies 

└── README.md 

 

## Using gazetteer and regex to extract places in the Gaza from the corpus 

The objective of the first task is to take all the place names from a collection of large number of news articles using the gazetteer which is a geographical index or dictionary. Then we have to improve the recognition of place names with the alternate names having other spellings from another column using regex techniques. After that we counted the number of times a name was mentioned per month in the articles after October 7, 2023. 

 

### Requirements  

You must have Python installed with the following libraries:  

re 

os 

Pandas 

  

You should also have Git Bash for version control  

git add . 

git commit -m “improved files” 

git pull 

git push  

  

### How the script works  

#### Reading and Preparing Data 

For the first task the script begins by importing necessary libraries. Our script uses re for matching patterns with regular expressions for finding all versions of the names. Os is used to navigate the file system and read articles in the articles folder and the pandas is used to organize and export data in tabular form. A function write_tsv() is defined in the beginning, which takes a list of data rows, column names, and file path and adds the data into tsv file using the panda’s library. This is done to make sure the output is clean and easy to analyze. 

Next the script loads a gazetteer which contains place names and their alternate forms. The script skips the header as the name column starts from the second row and processes each row to extract the names and alternate names which is listed in the 6th column. Any unnecessary spaces are also removed through the script. 

To ensure flexible matching of alternate names of a place, the script uses a single regular expression (regex pattern) for each place using | symbol which functions as “OR” in python. For example, for Gaza the other spellings could be Gazan or Gaza City, or it can also be in capital letters and the regex will combine all the three forms into one pattern. Each place name with its compiled pattern and a count of zero is then stored in a dictionary called patterns. 

#### Filtering and Analyzing Articles  

The script then processes the news articles which are stored in the folder. In the articles folder each file is saved with their respective dates in the format YYYY-MM-DD. The script uses this to filter out only those articles which were published before the war started on October 7, 2023. For each article after the start of war the code reads the content and uses regular expressions to search for matches of the place names and their alternates. We then use IGNORECASE to make sure that the script finds names regardless of capitalization. The total number of matches found for each place is added to the count stored in the patterns dictionary. In addition to counting the overall number of mentions, the script also checks how often each place was mentioned per month. It only includes the year and month part of the articles date to group mentions by month. This information is stored in a nested dictionary called mention_per_month, having a monthly count also.  

#### Displaying and Exporting the Results 

After all articles are processed, the script prints an output showing how many times each place was mentioned in each month. This is in a readable dictionary format. To prepare the data for external use, the script constructs a list of tuples, where each tuple contains the place name, month and the count. This list is then stored in the write_tsv file that we defined in the beginning, which saves the results into a file named regex_counts.tsv. 

  

### Sanity check  

After running the script check regex_counts.tsv file to make sure the output is correct. To check if the spellings were improved by regex, compared the missing or unmatched places with the gazetter. This helpes me see where the regex worked well and where it could still be improved. 

### Tips for Regex improvement 

While improving regex 

Use re.escape() to avoid errors with special characters 

Test patterns on regex website to make sure they worked properly. 

## Version control  

I made sure to regularly add, commit, and push my changes using Git Bash  

 

 

## Using Stanza Method to Extract Place Names (NER Method) 

The second part of this project uses Named Entity Recognition (NER) with the help of Stanza Library to extract place names. This part focused on identifying named entities under LOC (location), GPE (geo-political entities) for the articles published in January 2024. This process includes adapting to the notebook shared in class and making it useful for the full data in the portfolio repository. 

We made a copy of the Colab notebook, renamed it to Gaza_NER2_Kulsoom_Mahpara_Komal.ipynb and customized it to perform extraction of place names for a specific time interval. 

 

### How the Stanza Script Works 

#### Initial Setup and Libraries 

The notebook starts by installing stanza and initializing the English Language pipeline with NER capabilities. The data is read from the articles/ folder of the portfolio 

We used os to loop through all the text files and extract the data from filenames. A condition was set that only articles from January 2024 are selected for further processing. 

#### Named Entity Recognition using Stanza 

For each relevant article. The stanza pipeline is applied to extract named entities. We only collect those entities that are labeled as locations (LOC), and geopolitical entities (GPE). These extracted place names are sorted in dictionary, with a count of how many times each place name is mentioned in all the articles that are concerned. 

#### Cleaning and Normalization 

A standard_names dictionary was developed to minimize variation from different spelling variants or representation forms. The normalize_place() function removes all punctuations and "the" articles and possessive signs ("’s, 's") then converts to lower case while verifying dictionary entries. When no match is found the function applies an initial capital letter to each word. 

#### Saving and exporting the results 

Finally, the cleaned data is written into a file ner_counts_tsv inside the directory for further visualization and comparison 

### Version control 

Git add . 

Git commit -m “Added NER script and Output” 

## Geocoding Process 

Using Named Entity Recognition (NER) to extract and count place names from the corpus, the names were then translated into latitude and longitude coordinates so that mapping and visualization could be done.  I used the GeoNames API to geocode this. 

###Input Preparation 

Started with the “ner_counts.tsv” file because it had the clean place names and their counts. 

  

  

### Querying the GeoNames API 

For the places mentioned in the tsv file I brought their coordinates from the API geonames website: https://www.geonames.org/export/web-services.html accessing it through the free version by putting my username in the code.  

  

The script was doing the following functions: 

  

Requesting API for each place name 

Getting their latitude and longitude 

The places that had no coordination mark it NA. 

To avoid delays, adding a second delay between each request.  

  

###  Initial Gazetteer Output 

I compiled the results in `NER_gazetteer.tsv` which had three columns, the place name, latitude and longitude that the API returned.  NA was returned to places with no coordinates.  

  

###  Manual Review and Correction 

I opened the NER_gazetteer file and saw a lot of places with NA, some were misidentified as place names, and some were place names but their coordinates were missing. Below I have given the coordinates I added by google maps and the ones I deleted manually. I saved the same file after making these changes. 

  

### Files Involved 

  

| File                         | Description                                                    | 

|------------------------------|----------------------------------------------------------------| 

| `ner_counts.tsv`             | Place names and their counts from the NER extraction.          | 

| `NER_gazetteer.tsv`          | Initial geocoding results (with raw GeoNames API output).      | 

| `geocoding_script.py`        | The Python script that performed the automated geocoding.      | 

  

 

## Strengths and Limitations 

### Strengths 

It would have been difficult to go through each file and get the places’ name so a lot of time was saved to find the places’ name and their coordinates. Moreover, specific and easy steps were there to follow, only pathways needed mostly to be changed so they were not very complicated. 

  

### Limitations 

It skipped some places’ names even when they were places and had coordinates. It was missing from the database. Manually reviewing it was a limitation again as it was not highly accurate.  

## Possible Improvements 

More than one API like Google Maps could be added so that cross checking would be easy. Moreover, Google Collab could be upgraded so that it would run our codes faster because it was taking 30 minutes to run one code. 

## Mapping  

  

This part uses the regex-based extraction and NER extracted places to create maps. 

  

### Workflow Overview 

  

#### Regex Method: 

Using the `regex_counts.tsv` file merging it with the coordinate file, `geonames_gaza_selection.tsv` by using data = pd.merge(counts, coords, on=["placename/Place"]) 

  

  

#### NER Method 

Using the `NER_gazetteer.tsv` file merging it with the coordinate file, `NER_gazetteer.tsv` ` by using data = pd.merge(counts, coords, on=["placename/Place"]) 

  

#### Processing  

Both scripts process the data in the same way. Take out the whitespace from the column names, through conventions making the column names standardized and then converting it to numeric value. Lastly drop the rows that don’t have rows or coordinates.  

 

  

#### Visualization 

  

Using the library plotly express to make an interactive map. These include, giving it the size value, color and animations like hovering over the names.  

  

## Output of both maps 

 

### Regex-Extracted Places 

![Regex Map](file:///C:/Users/DELL/Downloads/FASDH25-portfolio2/regex_map.png) 

### NER-Extracted Places 

![NER Map](file:///C:/Users/DELL/Downloads/FASDH25-portfolio2/ner_map.png) 

### View outputs: 

Open outputs/NER_map.html or outputs/regex_map.html in any browser 

 

 

## Key Challenges 
 
**1. Overlapping Points**   
- *Now*: Manual zoom   
- *Future*: Leaflet.js clustering   
 
**2. Color Scale Variance**   
- *Now*: Independent scales   
- *Future*: Shared legend   
  
## Key Differences Between Approaches 

  

| Feature                | Regex Map                          | NER Map                          | 

|------------------------|------------------------------------|----------------------------------| 

| **Input**             | `regex_counts.tsv`                | `ner_counts.tsv`                | 

| **Gazetteer**         | Geonames Gaza subset              | Custom NER-specific gazetteer   | 

| **Temporal**          | Animated by month                 | Static aggregation              | 

| **Color Scale**       | Sequential YlOrRd                 | Default continuous scale        | 

| **Zoom**              | Automatic                         | Fixed initial zoom (level 2)    | 

  

## Compare the January 2024 maps generated from the regex- and NER data 
The Regex system found 15 locations using its pattern recognition system and the most occurring place appeared 4000 times. The NER system detected 18 locations in the data through machine learning but recorded less than half the maximum places mentioned compared to Regex. The regex maps display district trends better than other tools and let you compare changes to place names over individual months with their yellow-orange-red style. NER displays in-depth place details for both larger and smaller cities and towns, showing all complex names such as DERR EL-BALAH. Python tools Pandas and Plotly Express power both functions but Regex searches for bigger trends and NER finds specific details within text. Our study shows that blending these two techniques creates useful outcomes. Our results show that combining Regex timeline comparisons with NER place tag identification generates better results. We propose merging both datasets while creating 33 unique location sets and validating results against real maps, especially for data points that display significant discrepancies. The two analysis methods should work together since they have individual benefits that support geographic research better. 
 

 

## Advantages and Disadvantages of the Two Methods for Identifying Place Names in News Articles: 

  

### Advantages and disadvantages of Regex and Gazetteer method  

This method includes using a predefined list of place names in a gazetteer along with regular expressions to identify mentions of these locations in the articles. This method is more flexible as you can decide which names are going to be counted as places, which makes it useful for topics like the Gaza conflict where the same place is spelled in multiple ways. For example, Gaza, Gaza Strip and Gazan. We can add all of them to the list of alternate names to be able to recognize them.  

It is also quick, and we don’t need any complicated computer systems or libraries to make it work. It simply checks each article quickly to see if they have any of the place names from the list provided in the form of a gazetteer.  

One more thing is that it is easier to understand and fix if we run into any problems. For example, if a place name is missed or counted wrongly we can go back to the list and make changes. 

  

However, there are also some disadvantages of the method: 

The code only checks if a word matches a name from the list. It does not know the real meaning behind the word. For example, in case of Khan Younis it might match it as a persons name instead of a place name.  

The script also won’t match a place name if it is not present in the list or misspelled unless the exact name is present in the list or the regex pattern provided.  

Another problem with the regular expression in this code is that if it is used too generally it might also recognize a persons name as a place name and if it is used too narrow it might miss the name of the place also  which are spelled differently. 

  

### Advantages and disadvantages of Named Entity Recognition  

When we use Named Entity Recognition with tools such as Stanza, the biggest advantage id that the model understands the context. It means it doesn’t just look for exact words like in the gazetteer method, it tries to understand how the word is used in a sentence. For example, in case of Khan Younis regex method might misunderstand it as a person’s name however NER will try to look at the sentence where it has been used. For example, “Khan Younis is in the North of Gaza”, which makes the model understand that it is a place. But if the sentence says, “Khan Younis is reporting from Gaza”, it can tell that it is a person’s name not a place.  

Another benefit is that we don’t have to create a long manual list of place names like the one we did for regex and gazetteer method. It already knows many common locations, so it finds them for us. Moreover, it can also catch if there are spelling mistakes. 

 

However, there are some disadvantages of this model also: 

The model might miss lesser known or sensitive places like small areas in Gaza if it has not seen that name during training. Also, it confuses place names with organizations and people, like labeling the Gaza Health Ministry as a geopolitical entity rather than a government institution.  

Moreover, NER tools are also a bit slower and resource-heavy, as the code has to load large language models, which takes time to load and install and in the case of installing pip stanza. And when we are working with many articles, processing them with Stanza takes time as compared to regex method.  

While regex can be easily adjusted if there is a wrong code, it is harder to make changes in NER. If Stanza misses a name like “Al-Shati refugee camp”, we can’t just add it to the list of names. We will have to retrain the model, which is not easy to do.  

 

 

## Self-Critical Analysis: 

One of the main weaknesses of our project is that the regex method works well only for those names which are written exactly the same or matches one of the alternate spellings listed in our gazetteer. If a different place is mentioned with different spelling or local names that we did not include are mentioned the code will miss that. This means we are depending on how complete and accurate our gazetteer is. And our gazetteer does not cover all the possible names. Also if a new location comes up in the news after we have built the gazetteer, the code won’t be able to detect that unless we modify it manually.  

With the named entity recognition, we faced similar issues. NER can only identify names it was trained to recognize. For example, it doesn’t understand “US” unless we tell it ourselves that it stands for “United States”. We added some of these short forms manually but it’s likely we missed others.  

Another issue is with geocoding, sometimes the code confused place names with organization names or treated organizations as locations. This created errors in the final results. For example, it might think of an NGO or news outlet as a place. 

In terms of mapping the map created using NER did not show changes in the place name mentioned over time. We were shown basic mapping tools but with more time and skills, the map could have been more detailed and interactive. 

If more time was available, there are many things that we can improve. First, we could expand our gazetteer by adding more local names and variations of place names. This would make the regex method much more effective. For the alternate spellings we could use more names and make multiple regex patterns to make sure it doesn’t miss any of the spellings.  

To improve NER we could train a new model on news articles from the Gaza war, so it learns the unique names and terms in that context. We could also add more names or short forms manually as we would have had enough time to go through the articles. 

We could also build better maps that show how the place mentions changes over time. For example an interactive map that updates month by month, which would help us understand how media attention shifts geographically as the conflict continues.  

With these improvements the project can be complete and more accurate. 

 

 

 

 
