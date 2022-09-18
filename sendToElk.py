from turtle import home
import requests
import os
import yaml
config={}
with open("./config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
print(config["input"])


print('{}/{}/_bulk'.format(config["host"],config["index"]))
# Get the list of all files and directories
# in the root directory
path = "./Outputs/"+config["output"]
dir_list = os.listdir(path)
print(dir_list)


headers = {
    'Content-Type': 'application/x-ndjson',
}

# reads broken up files from directory /output/index_name
for i in dir_list:
    with open('./output/{}/{}/{}'.format(config["output"],config["index"],i), 'rb') as f:
        data = f.read()

    response = requests.post('{}/{}/_bulk'.format(config["host"],config["index"]), headers=headers, data=data, auth=(config["user"],config["password"]))
    print(response)