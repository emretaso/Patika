##Equivalent Key Presser
q = ["", "-B,-B,-B"]
a,b =  list(map(lambda x: x.split(","), q))

delete1 = []
delete2 = []

for no, key in enumerate(a):
    if key == '-B':
            delete1.extend([no-1, no])
t1 = [z for x, z in enumerate(a) if not x in delete1 and z != '']

for no1, key2 in enumerate(b):
    if key2 == '-B':
            delete2.extend([no1-1, no1])
t2 = [z for x, z in enumerate(b) if not x in delete2 and z != '']

if t1 == t2:
    print(True)
else: print(False)
