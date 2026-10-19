print("\n")
print("Select One Option From The Following -\n\n")
print("Area Of A Shape (Type-A)\n")
print("Perimeter Of A Shape (Type-P)\n")

select = input("Enter The Option : ")

if select.lower() == 'a':
    print("Area Of Circle (Type-AC)\n")
    print("Area Of Square (Type-AS)\n")
    print("Area Of Rectangle (Type-AR)\n")
    print("Area Of Triangle (Type-AT)\n")

elif select.lower() == 'p':
    print("Perimeter/Circumference Of Circle (Type-PC)\n")
    print("Perimeter Of Square (Type-PS)\n")
    print("Perimeter Of Rectangle (Type-PR)\n")
    print("Perimeter Of Equilateral Triangle (Type-PET)\n")
    print("Perimeter Of Isosceles Triangle (Type-PIT)\n")
    print("Perimeter Of Scalene Triangle (Type-PST)\n")

calc = input("Enter The Option : ")

if calc.lower() == 'ac':
    r = float(input("Enter The Radius : "))
    print("Area Of Circle is :", 3.14 * r * r)

elif calc.lower() == 'pc':
    r = float(input("Enter The Radius : "))
    print("Perimeter/Circumference Of Circle is :", 2 * 3.14 * r)

elif calc.lower() == 'as':
    l = float(input("Enter The Length Of Side : "))
    print("Area Of Square is : ", l * l)

elif calc.lower() == 'ps':
    l = float(input("Enter The Length Of Side : "))
    print("Perimeter Of Square is :", 4 * l)

elif calc.lower() == 'ar':
    le = float(input("Enter The Length : "))
    br = float(input("Enter The Breadth : "))
    print("Area Of Rectangle is :", le * br)

elif calc.lower() == 'pr':
    le = float(input("Enter The Length : "))
    br = float(input("Enter The Breadth : "))
    print("Perimeter Of Rectangle is :", 2 * (le + br))

elif calc.lower() == 'at':
    h = float(input("Enter The Height : "))
    ba = float(input("Enter The Length Of Base : "))
    print("Area Of Triangle is :", 0.5 * h * ba)

elif calc.lower() == 'pet':
    s = float(input("Enter The Length Of Side : "))
    print("Perimeter Of Equilateral Triangle is :", 3 * s)

elif calc.lower() == 'pit':
    es = float(input("Enter The Equal Side Length : "))
    ts = float(input("Enter The Length Of 3rd side : "))
    print("Perimeter Of Isosceles Triangle is :", (2 * es) + ts)

elif calc.lower() == 'pst':
    so = float(input("Enter The Length Of 1st Side : "))
    st = float(input("Enter The Length Of 2nd Side : "))
    sth = float(input("Enter The Length Of 3rd Side : "))
    print("Perimeter Of Scalene Triangle is :", so + st + sth)

else:
    print("Invalid option selected")
