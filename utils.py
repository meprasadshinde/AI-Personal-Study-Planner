import json

def load_data():
    with open("sample_input.json", "r") as file:
        data = json.load(file)

    return data["subjects"], data["hours_per_day"]