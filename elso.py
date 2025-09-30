x = float(input("Add meg az első oldal hosszát: "))
y = float(input("Add meg a második oldal hosszát:"))
z = float(input("Add meg a harmadik oldal hosszát:"))
 
if ((x + y) > z)and((x + z) > y) and((y + z) > x):
    print("Csinálható")
else:
    print("Nem csinálható")
