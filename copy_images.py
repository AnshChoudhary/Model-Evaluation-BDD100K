import os
import csv
import shutil

# Path to the CSV file
csv_path = "/data/BDD100K/bdd100k/night_images.csv"

# Source folder containing the 10,000 images
source_folder = "/data/BDD100K/bdd100k/images/100k/val"

# Destination folder to copy the matching images
destination_folder = "/data/BDD100K/bdd100k/night/images"

# Create the destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Read the CSV file and get the list of filenames
with open(csv_path, "r") as csvfile:
    reader = csv.reader(csvfile)
    # Skip the header
    next(reader, None)
    filenames = [row[0] for row in reader]

# Copy the matching images to the destination folder
for filename in filenames:
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, filename)
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f"Copied: {filename}")
    else:
        print(f"File not found: {filename}")

print("Copying completed.")