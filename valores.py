def main():
    a = int(input("introduce el valor de a:"))
    b = int(input("introduce el valor de b:"))

aux = b
b = a
a =  aux
print(a)
print(b)