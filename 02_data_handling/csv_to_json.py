import os
import json
import csv

INPUT_FILE = "converted_data.csv"
OUTPUT_FILE = "converted_data.json"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return []
    
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
        print(data)
        return data
    
def save_as_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    print(f"✅ Converted {len(data)} record to {filename} successfully")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))

def main():
    print("Converting CSV to JSON ..")
    data = load_csv_data(INPUT_FILE)
    if not data:
        return
    save_as_json(data, OUTPUT_FILE)
    preview_data(data)

if __name__ == "__main__":
    main()