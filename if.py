unik = False
pokusy = 3
while True:

    print("1 - prohledat stůl")
    print("2 - zkusit otevřít dveře")
    print("3 - podívat se pod koberec")

    volba = input("co udeláš?")

    if volba == "1":
        print("našel jsi kód 123")
    elif volba == "2":
        kod = input("zadejte kod:") 
        if kod == "123":
                unik = True 
        else: 
            print("špatné heslo")
            pokusy = pokusy-1
    elif volba == "3":
        print("nic si nenašel")
    else:
        print("neplatná možnost")
    if unik == True:
            print("utekl jsi")
    else:
        print("prohral jsi")               
