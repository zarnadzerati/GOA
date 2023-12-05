def triangles(a,b,c):
    
    if a + b > c and a + c > b and b + c > a:
        print("ასეთი სამკუთხედი იარსებებს")
    else:
        print("ასეთი სამკუთხედი ვერ იარსებებს")

triangles(4,7,7)
triangles(3,1,5)
triangles(6,2,3)