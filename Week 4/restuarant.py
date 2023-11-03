import json
from datetime import datetime
from functools import reduce

import json

# Open the input file
with open(r"C:\Users\marno\Wiley Edge\Code\Week 4\restaurant.json", "r") as input_file:
    lines = input_file.readlines()

# Initialize an empty list to store JSON objects
json_objects = []

# Initialize an empty string to accumulate JSON text
current_json = ""

# Process each line
for line in lines:
    # If the line is not empty, add it to the current JSON text
    if line.strip():
        current_json += line.strip()
    else:
        # If the line is empty, parse the current JSON text and append it to the list
        if current_json:
            try:
                json_object = json.loads(current_json)
                json_objects.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON: {e}")
        current_json = ""

# If there's remaining JSON text in the current_json, parse and append it
if current_json:
    try:
        json_object = json.loads(current_json)
        json_objects.append(json_object)
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")

# Write the list of JSON objects to an output file
with open("output.json", "w") as output_file:
    json.dump(json_objects, output_file, indent=2)

print("Conversion complete. JSON data written to 'output.json'.")
