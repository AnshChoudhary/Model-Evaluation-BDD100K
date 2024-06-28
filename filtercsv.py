import csv
import json

labels_path = "/data/BDD100K/bdd100k/labels/det_20/bdd100k_labels_images_val.json"

output_csv_path = "filtered_images.csv"

with open(labels_path,"r") as file:
    data = json.load(file)

night_images = []

for item in data:
    if item["attributes"]["timeofday"] == "night":
        night_images.append(item["name"])

with open(output_csv_path, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filename"])
    for filename in night_images:
        writer.writerow([filename])

print(f"Filtered images have been written to {output_csv_path}")