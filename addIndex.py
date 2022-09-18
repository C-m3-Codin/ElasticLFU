
file = open("./Broken_sr-api-internal-laravel/file3.json","r")
lines = file.readlines()

writeFiles=open("./Broken_sr-api-internal-laravel/file.json","w")

j=0
for i in lines:
    print(j)
    j=j+1
    writeFiles.write('{"index": {"_index": "some_other"}} \n')
    writeFiles.write(i)

writeFiles.close()
file.close()
    
