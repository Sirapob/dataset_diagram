import json
import base64
import os
import csv

image_folder: str = 'dataset/images'

# CSV file containing descriptions
csv_file = 'dataset/dataset.csv'

# Read description from CSV file
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    descriptions = {row['image']: row['text'] for row in reader}

# List to hold encoded images
encoded_images = []

# Encode each image in the folder to base64
for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    with open(image_path, 'rb') as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        description = descriptions.get(image_name, "No description available")
        encoded_images.append({
            "filename": image_name,
            "description": description,
            "image": encoded_image
        })

# Data to be written to JSON file
data = {
    "images": encoded_images
}

# Write data to JSON file
with open('dataset/solution_diagram.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)