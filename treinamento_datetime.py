# treinamento do datetime

from datetime import date, time, datetime, timedelta

ano = date.today().year
mes = date.today().month
dia = date.today().day
data = date.today()
hora = datetime.now()
hora2 = datetime(2022,9,3,3,00)
bday = datetime(2022,9,15,00,00)

print(ano)
print(mes)
print(dia)
print(data)
print(hora)
print(hora2)
print(bday)
tqualquer = hora2 - hora
print(tqualquer)
diferenca= bday - hora
print(f"Seu aniversário é daqui à {diferenca}")
tdays = diferenca.days
print(f"Seu aniversário é m {tdays} dias")
tses = diferenca.total_seconds()
print(f"tempo em segundos: {tses:.0f}")
tmin = tses / 60
thora = tses / (60*60)
tdias = int(thora / 24)
print(f"tempo em minutos: {tmin:.0f}")
print(f"tempo em horas: {thora:.0f}")
print(tdias)

hora1 = 3600

hora6 = 21600
hora12 = 43200
hora18 = 64800
hora24 = datetime.now() + timedelta(days=1)
hora30 = 108000


string=str(tqualquer)
output=string.split()
print(output)
if "-" in output[0]:
    print("Você não pode reservar com uma data passada")

#converter datetime.now()

hoje = datetime(date.today().year, date.today().month, date.today().day, 2, 2, 2)
print(f"data e hora hoje: {hoje}")
dia2 = datetime(2023,2,25,3,00)
difa = dia2 - hora
print(difa)
tses2 = difa.total_seconds()

futuro = datetime.now() + timedelta(days=tdias)
print(futuro)

hoje = datetime(date.today().year, date.today().month, date.today().day, 0, 0, 0)
escolha = datetime(2023, 2, 29, 0, 0, 0)
print(escolha)






