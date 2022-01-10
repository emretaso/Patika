a="Hello Patika*DEV-  uSEr"
import string
y=[]
for x in a:
    if x not in list(string.ascii_uppercase) and x not in list(string.ascii_lowercase):
        y.append("")
    else:
        y.append(x)

q=[]
for t in range(len(y)):
    if y[t]!="":
        if t==0:
            q.append(y[t].upper())
        elif y[t-1] !="":
            q.append(y[t].lower()) 
        else:
            q.append(y[t].upper())
print("".join(q))