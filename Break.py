import ast
import json

file1 = open('BiggerJson.json', 'r')
Lines = file1.readlines()
index = "something"

writeFileName='./Brokensr-api-internal-laravel/file{}.json'
# writeFiles.write()
j=1
f = open(writeFileName.format(j), 'w')
  # python will convert \n to os.linesep
count=0
for line in Lines:
    # if(count==100):
    #     break
    count=count+1
    line = line[line.find("sourc")+9:-2]
    a=ast.literal_eval(line)
    js=json.dumps(a)

    print(count)
    if(count%5000==0):
        print("newFile Here",count)
        j=j+1
        f.close()
        f = open(writeFileName.format(j), 'w')
    f.write('{"index": {"_index": "sr-api-internal-laravel" } } \n')
    f.write(js)
    f.write("\n")




