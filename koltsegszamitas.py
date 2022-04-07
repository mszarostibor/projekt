def szamitas():
    lista=[]
    listaosszeg=[]
    i=1
    while i<5:
      a=input("Adjon meg egy terméket: ")
      lista.append(a)
      if a=="0":
        break
      V=int(input("Adja meg a termék mennyiségét: "))
      VV=int(input("Adja meg a termék árát: "))
      listaosszeg.append(V * VV)
      print("Ha be akkarja fejezni a müveletett akkor írja be 0")

      
    for i in range(len(lista)):
      if lista[i]=="0":
        break
      print(lista[i]," összege: ",listaosszeg)
      
  
szamitas()
