"""
This is the maps for NER cont file.

It reads place mention counts and coordinates,
merges them, and visualizes them on an interactive map.
"""

import pandas as pd
import plotly.express as px

# Load the counts data (from NER output) and the gazetteer with coordinates
counts = pd.read_csv("ner_counts.tsv", sep="\t")
coords = pd.read_csv("gazetteers/NER_gazetteer.tsv", sep="\t")

# Clean column names: remove any unexpected leading/trailing whitespace
counts.columns = counts.columns.str.strip()
coords.columns = coords.columns.str.strip()

# Rename columns in the gazetteer to match the counts data and plotting library requirements
coords = coords.rename(columns={
    "Name": "Place",           # Standardize place name column
    "Latitude": "latitude",    # Match expected name for latitude
    "Longitude": "longitude"   # Match expected name for longitude
})

# Merge the counts and coordinates data on the place name
# - Left table: 'placename' from counts
# - Right table: 'Place' from coords
data = pd.merge(counts, coords, left_on="Place", right_on="Place")

# Convert the 'count' column to numeric (non-numeric values become NaN)
data["count"] = pd.to_numeric(data["Count"], errors="coerce")

# Drop rows with missing essential values (to avoid errors in plotting)
data = data.dropna(subset=["count", "latitude", "longitude"])

# Create a scatter map:
# - Each place is a point on the map
# - Point size and color reflect the count of mentions
# - Hover text shows the place name
fig = px.scatter_map(
    data,
    lat="latitude",
    lon="longitude",
    hover_name="Place",
    size="count",
    color="count",
    title="NER-extracted Places",
    zoom=2,  # Set an initial zoom level (world view)
)

# Display the interactive map
fig.show()

# Save the map as an HTML file for sharing/viewing outside Python
fig.write_html("NER_map.html")
