def lee_entero():
   while True:
       entrada = raw_input("Escribe un numero entero: ")
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           print ("La entrada es incorrecta: escribe un numero entero")