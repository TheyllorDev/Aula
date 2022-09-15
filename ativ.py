while True:

    numero = input ("Digte um numero. \n")

    try:
        numero = int (numero)
        
    except: 
        print ("Tente novamente.")
        continue

    numero2 = input ("Digte outro numero. \n")
    
    try:
        numero2 = int (numero2)
        
    except: 
        print ("Tente novamente.")
        continue

    operacao = input ("Que tipo de operação você gostaria de fazer? \n")

    if (operacao == "+"):
        print (numero + numero2)

    elif (operacao == "-"):
        print (numero - numero2)

    elif (operacao == "*"):
        print (numero * numero2)

    elif (operacao == "/"):
        try:
            print (numero / numero2)

        except:
            print ("Impossível dividir.")

    parar = (input ("Gostaria de parar o loop?\n"))

    if (parar == "Sim" or parar == "sim" or parar == "S" or parar == "s"):
        break