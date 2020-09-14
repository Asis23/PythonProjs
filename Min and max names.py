x = str (input ("Key in your name:"))
if len(x) < 3:
    print ("your name is too short")
elif len(x) > 50:
    print ("your name is too long")
else:
    print ("name looks good!")