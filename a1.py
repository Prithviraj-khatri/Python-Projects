f = open("poem.txt")
c = f.read()
if("twinkle" in c):
    print("present")
else:
    ("not present")
f.close()