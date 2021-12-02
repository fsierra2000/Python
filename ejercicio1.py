def main():

    num = int(input("introduce un numero:"))

    while num < 1:
        print("NO es natural")
        num = int(input("introduce un numero"))

    print("es natural")