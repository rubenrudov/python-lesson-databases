import json

json_file = open("db.json", "r")

DATABASE = json.load(json_file)
print(DATABASE)

json_file.close()  # Closing the file

UPDATE_DICT = DATABASE
UPDATE_DICT["Guy"] = "Elram"

with open("db.json", "w") as json_file:
    json.dump(UPDATE_DICT, json_file, indent=2)


