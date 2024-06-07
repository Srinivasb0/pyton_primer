
import json
data = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": False,
            "age": 8
        }
    ]
}

json_convert = json.dumps(data, indent=4, sort_keys=True)
print(json_convert)