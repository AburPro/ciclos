# while True:
#     lista=[]
#     ingMins=float(input('ingrese los tiempos de cada tramo cuando quiera finalizar ingrese 0\n'))
#     hora=round(ingMins/60)
#     min=(ingMins / 60) * 60
#     lista.append(ingMins)
# for i in lista:
#     print(ingMins)
#     print(lista)
# if ingMins==0:
#     break


hora=[]
minutos=[]
while True:
    ask=float(input('Ingrese los minutos de viaje o 0 para finalizar\n-> '))
    if ask == 0:
        break
    if ask < 60:
        minutos.append(ask)
    elif ask%60 == 0:
        hora.append(ask/60)
    elif ask%60 != 0:
        horaH=round(ask/60)
        hora.append(horaH)
        minutosM=round(((ask/60)*60)-60*horaH)
        minutos.append(minutosM)
    if ask==0:
        break
print(f"tiempo total del viaje: {sum(hora)} :{sum(minutos)}")
