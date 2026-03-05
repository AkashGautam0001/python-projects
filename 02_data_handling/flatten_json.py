import json
import os

INPUT_FILE="nested_data.json"
OUTPUT_FILE="flattened_data.json"

def flatten_json(data, parent_key="", sep="."):
    items = {}

    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.update(flatten_json(v, full_key, sep=sep))

    elif isinstance(data, list):
        for i, v in enumerate(data):
            full_key = f"{parent_key}{sep}{i}" if parent_key else str(i)
            items.update(flatten_json(v, full_key, sep=sep))
    else:
        items[parent_key] = data
    return items

def main():
    if not os.path.exists(INPUT_FILE):
        print("JSON file not found")
        return
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        sep = input("Enter the separator for the flattened keys (default is .): ").strip() or "."

        flattened_data = flatten_json(data,"", sep)
            
        with open(OUTPUT_FILE, "w", encoding="utf-8") as output_file:
            json.dump(flattened_data, output_file, indent=2)
        
        print(f"✅ Converted {INPUT_FILE} to {OUTPUT_FILE} successfully")
    except json.JSONDecodeError:
        print("Invalid JSON format")

if __name__ == "__main__": main()