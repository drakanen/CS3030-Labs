import json, yaml
json_string = ('{"server": "prod",'
               ' "port": 80,'
               ' "status": "active"}')
python_data = json.loads(json_string)
jsonFormatted = json.dumps(python_data, indent=2)

#Write the .json script
with open("config.json", "w") as outfile:
    outfile.write(jsonFormatted)

#Read it back
with open("config.json", "r") as readJson:
    data = json.load(readJson)
    data["status"] = "maintenance" #Change status

#Write to .yaml
with open("config.yaml", "w") as outfile:
    yaml.dump(data, outfile, default_flow_style=False)