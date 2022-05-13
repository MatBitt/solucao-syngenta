def get_cheapest_hotel(entrada):   #DO NOT change the function's name
    lakewood = 3
    bridgewood = 4
    ridgewood = 5
    precos_hoteis = []

    entrada = entrada.replace(",", "")
    entradas = entrada.split()

    cliente = entradas[0]
    tipo_de_cliente = (1 if cliente == "Rewards:" else 0)
    # print("Cliente :", cliente)
    estadias = entradas[1:]
    # print("Estadias :", estadias)

    precos_hoteis.append( get_custo_hotel(estadias, tipo_de_cliente, lakewood) )
    precos_hoteis.append( get_custo_hotel(estadias, tipo_de_cliente, bridgewood) )
    precos_hoteis.append( get_custo_hotel(estadias, tipo_de_cliente, ridgewood) )

    precos_hoteis.sort()

    return desempate(precos_hoteis)

def get_custo_hotel(estadias, cliente, hotel):
    total = 0
    reward = 1
    lakewood = 3
    bridgewood = 4
    ridgewood = 5

    for estadia in estadias:
        dia = estadia[-4:-1]
        fim_de_semana = (1 if dia == "sat" or dia =="sun" else 0)

        if(fim_de_semana):
            if(cliente == reward):
                if(hotel == lakewood):
                    total += 80
                if(hotel == bridgewood):
                    total += 50
                if(hotel == ridgewood):
                    total += 40
            else:
                if(hotel == lakewood):
                    total += 90
                if(hotel == bridgewood):
                    total += 60
                if(hotel == ridgewood):
                    total += 150
        else:
            if(cliente == reward):
                if(hotel == lakewood):
                    total += 80
                if(hotel == bridgewood):
                    total += 110
                if(hotel == ridgewood):
                    total += 100
            else:
                if(hotel == lakewood):
                    total += 110
                if(hotel == bridgewood):
                    total += 160
                if(hotel == ridgewood):
                    total += 220
    return (total, hotel)

def desempate(precos):
    lakewood = 3
    bridgewood = 4
    ridgewood = 5
    hoteis_empatados = []

    for hotel in precos:
        if hotel[0] == precos[0][0]:
            hoteis_empatados.append(hotel)
    
    hoteis_empatados.sort(key=lambda y: y[1])

    ganhador = ''
    if(hoteis_empatados[-1][1] == lakewood):
        ganhador = 'Lakewood'
    elif(hoteis_empatados[-1][1] == bridgewood):
        ganhador = 'Bridgewood'
    if(hoteis_empatados[-1][1] == ridgewood):
        ganhador = 'Ridgewood'

    return ganhador
