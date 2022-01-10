##Equivalent Key Presses Have the function Equivalent Keypresses(stArr) read the array of strings stored in strArr which will contain 2 strings representing two comma separated lists of keypresses. Your goal is to return the string true if the keypresses produce the same printable string and the string false if they do not. A keypress can be either a printable character or a backspace represented by -B. You can produce a printable string from such a string of keypresses by having backspaces erase one preceding character.

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