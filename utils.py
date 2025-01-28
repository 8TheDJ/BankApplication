import json
import os

def load_data(file_path="data.json"):
    """Load data from the JSON file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Data file is corrupted. Starting fresh.")
                return {}
    return {}

def save_data(data, file_path="data.json"):
    """Save data to the JSON file."""
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
