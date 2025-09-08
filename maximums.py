def max_of_two(x, y):
    if x >= y:
        return x
    else:
        return y

def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z

# max_of_two (3 veces)
print("Probando max_of_two")
x = int(input("Ingresa x: "))
y = int(input("Ingresa y: "))
print("El mayor es:", max_of_two(x, y))

x = int(input("Ingresa x: "))
y = int(input("Ingresa y: "))
print("El mayor es:", max_of_two(x, y))

x = int(input("Ingresa x: "))
y = int(input("Ingresa y: "))
print("El mayor es:", max_of_two(x, y))

# max_of_three (3 veces)
print("\nProbando max_of_three")
x = int(input("Ingresa x: "))
y = int(input("Ingresa y: "))
z = int(input("Ingresa z: "))
print("El mayor es:", max_of_three(x, y, z))

x = int(input("Ingresa x: "))
y = int(input("Ingresa y: "))
z = int(input("Ingresa z: "))
print("El mayor es:", max_of_three(x, y, z))

x = int(input("Ingresa x: "))
y = int(input("Ingresa y: "))
z = int(input("Ingresa z: "))
print("El mayor es:", max_of_three(x, y, z))
