import json
file='E:\\gitHub\\python\\xyz.json'
var=[]
with open(file) as f:
    var=json.load(f)
    var['apiVersion']='v2'

with open(file,'w') as f1:
    json.dump(var,f1)

print(var)
