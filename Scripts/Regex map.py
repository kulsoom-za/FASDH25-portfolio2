import pandas as pd
import plotly.express as px

# Load the place mention counts from a TSV file
counts = pd.read_csv("Scripts/regex_counts.tsv", sep="\t")

# Load the gazetteer with place names and their coordinates
coords = pd.read_csv("gazetteers/geonames_gaza_selection.tsv", sep="\t")

# Remove any leading/trailing spaces in the column names for consistency
counts.columns = counts.columns.str.strip()
coords.columns = coords.columns.str.strip()

# Rename columns in the gazetteer to match the counts data for merging
coords = coords.rename(columns={
    "asciiname": "placename",
    "latitude": "latitude",
    "longitude": "longitude"
})

# Merge the counts data with coordinates based on the common 'placename' column
data = pd.merge(counts, coords, on="placename")

# Convert the 'count' column to numeric (in case of non-numeric values, they become NaN)
data["count"] = pd.to_numeric(data["count"], errors="coerce")

# Drop rows with missing values in essential columns ('count', 'latitude', 'longitude')
data = data.dropna(subset=["count", "latitude", "longitude"])

# Create an animated scatter map:
# - Each point shows a place, with size and color representing the count of mentions
# - The map animates over time using the 'month' column to step through frames
fig = px.scatter_map(
    data,
    lat="latitude",
    lon="longitude",
    hover_name="placename",  # Hover text shows place name
    size="count",            # Bubble size reflects count
    animation_frame="month", # Create a frame for each month
    color="count",           # Bubble color also reflects count
    color_continuous_scale=px.colors.sequential.YlOrRd,
    title="Regex-Extracted Place Map"
)


# Save the map as an interactive HTML file so it can be opened in a browser
fig.write_html("regex_map.html")

# Display the map directly in the notebook or script (if supported)
fig.show()
