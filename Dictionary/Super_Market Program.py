supermarket={"store1":{'name':"smruti general store",'items':[ {'name':'soap',"quantity": 20},{"name":"brush","quantity":30},{"name":"pen","quantity":50}]},
             "store2":{"name":"tapasweeni store","items":[{"name":"python","quantity":100},{"name":"django","quantity":50},{"perfume":"Titan","quantity":60}]}}
print(supermarket["store2"]["name"])
for d in supermarket["store1"]["items"]:
    print(d["name"])
for d in supermarket["store2"]["items"]:
    if d["name"]=='django':
        print(d["quantity"])
for d in supermarket["store1"]["items"]:




