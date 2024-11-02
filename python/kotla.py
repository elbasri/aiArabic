chai = 500
if (chai >= 355):
    if chai <= 500:
        chai = 0
        print("salina: {}".format(chai))

ism = input("Ma ismok ?")
if (ism == "Nacer"):
    print("Salam ", ism)

elif(ism != "Ahmed"):
    print("Malk mglob? ", ism)
else:
    print("Ahlan ", ism)
omr = int(input("Ch7al omrek?"))
exit("Nta sghir sir t9ra l7orof")  if omr < 12 else print("aji t3allam paython")

match omr:
    case 15 | 16 | 17 | 14 | 13 | 12:
        print("ghadi tbda bchwia bchwia")
    case 18 | 19 | 20:
        print("jri chwia")
    case _:
        print("3ndek nhar wa7ed a7nini !")