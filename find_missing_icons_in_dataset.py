import pandas as pd

# Load icons from 'falist.txt'
with open('falist.txt', 'r') as file:
    falist_icons = [line.strip() for line in file.readlines()]

# Load the first column of 'icon_associations.csv' to get the list of icons in it
try:
    df = pd.read_csv('icon_associations.csv', usecols=[0], header=None)
    csv_icons = df[0].tolist()
except FileNotFoundError:
    print("The file 'icon_associations.csv' does not exist.")
    csv_icons = []

# Convert to set for faster lookup
csv_icons_set = set(csv_icons)

# Check each icon from 'falist.txt' against the icons in 'icon_associations.csv'
missing_icons = [icon for icon in falist_icons if icon not in csv_icons_set]

# Output missing icons
if missing_icons:
    print("Missing icons from 'icon_associations.csv':")
    for icon in missing_icons:
        print(icon)
else:
    print("All icons from 'falist.txt' are present in 'icon_associations.csv'.")
