x = int (input ("Weight:"))
y = str (input("(L)bs or (K)gs)?"))

if y.lower() == "k":
    convert = x / .45
    print (f" you are {convert} pounds")
else:
    convert = x * .45
    print (f"you are {convert} kilos")