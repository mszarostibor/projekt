def szamitas():
    lista=[]

    router = int(input("Egy router ára: ")) * int(input("A routerek száma: "))
    laptop = int(input("Egy laptop ára: ")) * int(input("A laptopok száma: "))
    szerver = int(input("Egy szerver ára: ")) * int(input("A szerverek száma: "))
    pc = int(input("Egy pc ára: ")) * int(input("A pc-k száma: "))
    mobil = int(input("Egy mobil ára: ")) * int(input("A mobilok száma: "))
    nyomtato = int(input("Egy nyomtató ára: ")) * int(input("A nyomtatók száma: "))

    lista.append(router)
    lista.append(laptop)
    lista.append(szerver)
    lista.append(pc)
    lista.append(mobil)
    lista.append(nyomtato)
    print("A routerek ára:",lista[0], "Ft")
    print("A laptopok ára:",lista[1], "Ft")
    print("A szerverek ára:",lista[2], "Ft")
    print("A pcék ára:",lista[3], "Ft")
    print("A mobilok ára:",lista[4], "Ft")
    print("A nyomtatók ára:",lista[5], "Ft")


szamitas()
