"""Geocoding Module

This module reads place names from a TSV file, uses the GeoNames API to get their coordinates,
and writes the results to a new TSV file.

The main steps are:
1. Reading place names from an input TSV file.
2. Fetching coordinates (latitude and longitude) for each place using the GeoNames API.
3. Saving the place names with their coordinates into a new TSV file.
"""

import requests
import time

# Set your GeoNames username (required for API access)
geonames_username = "kulsoom_zaman"

def get_coordinates(place, username=geonames_username, fuzzy=0, timeout=1):
    """
    Gets a single set of coordinates (latitude and longitude) for a given place using the GeoNames API.

    Args:
        place (str): The name of the place to geocode.
        username (str): GeoNames username for API access. Default is set globally.
        fuzzy (int): The fuzziness level for name matching (default is 0 for exact match).
        timeout (int): Seconds to wait between API calls to avoid overwhelming the server (default 1).

    Returns:
        dict: A dictionary with 'latitude' and 'longitude'. If no result is found, returns 'NA' for both.
    """
    time.sleep(timeout)  # Avoid making rapid requests to the API
    url = "http://api.geonames.org/searchJSON?"
    params = {
        "q": place,
        "username": username,
        "fuzzy": fuzzy,
        "maxRows": 1,
        "isNameRequired": True
    }
    response = requests.get(url, params=params)
    # convert the response into a dictionary:
    results = response.json()
    print(results)
# get the first result:
    try:
        result = results["geonames"][0]  
        return {"latitude": result["lat"], "longitude": result["lng"]}
    except (IndexError, KeyError):
        # Return 'NA' if no valid coordinates found
        return {"latitude": "NA", "longitude": "NA"}  

# An empty list to hold place names
places = []
with open("ner_counts.tsv", 'r', encoding="utf-8") as file:
    next(file)  # Skip header
    for line in file:
        line = line.strip()
        if not line:   # Skip empty lines (common fix)
            continue
        # Take first column even if tab is missing (ChatGPT-3)
        name = line.split("\t")[0]  #  Only take first column
        places.append(name)

# Prepare a list to hold the place names with their coordinates
coordinates_result = []

# get the coordinates for each placefor place_name in places:
for place_name in places:
    coordinates = get_coordinates(place_name)
    if coordinates:
        latitude = coordinates["latitude"] #help from Chatgpt 2
        longitude = coordinates["longitude"] #help from Chatgpt 2
        coordinates_result.append((place_name, latitude, longitude))
   

    # Print the coordinates to track progress
    print(f"{place_name}: {coordinates['latitude']}, {coordinates['longitude']}")

with open("NER_gazetteer.tsv", mode="w", encoding="utf-8") as file:
    header = "Place\tlatitude\tlongitude\n"
    file.write(header)
    for name, latitude, longitude in coordinates_result: # Chatgpt help 1
        row = f"{name}\t{latitude}\t{longitude}\n"
        file.write(row)

