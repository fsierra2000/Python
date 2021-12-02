def main():
    aux = aux2 = 0
    num = int(input("introduce un numero entero:"))
    while num < 1:
        num = int(input("introduce un numero entero:"))
    for x in range(num):
        aux += x
        if aux < num:
            print(x, end="")
            aux2 += x

    print("la suma de los valores es", aux2)

if __name__ =="__main__":
    main()