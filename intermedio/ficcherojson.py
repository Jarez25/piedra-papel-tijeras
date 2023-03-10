import json

json_file = open("intermedio/my_json.json", "w+")

json_text = {"nombre":"jairo","apellido":"medina","edad":24, "lenguaje":"python"}

json.dump(json_text, json_file,indent= 4)

json_file.close()

with open("intermedio\my_json.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("intermedio\my_json.json"))
print(json_dict)
print(type(json_dict))
print(len(json_dict))
print(json_dict['nombre'])