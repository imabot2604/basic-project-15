import json
def format_json(d): return json.dumps(d, indent=4)
if __name__ == "__main__":
    print(format_json({"key": "value"}))
