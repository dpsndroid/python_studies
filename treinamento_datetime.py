# treinamento do datetime

from datetime import date, time, datetime, timedelta
from time import strptime

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
escolha = datetime(2023, 2, 27, 0, 0, 0)
print(escolha)
print("-------------------------------------------------------------------------------------")

data_inicial = "06/09/2022" 

dataret = data_inicial.split("/")
print(dataret)
x = int(dataret[0])
y = int(dataret[1])
z = int(dataret[2])
dataret2 = [x,y,z]
print(dataret2)



datar = "07/09/2022"
datad = "08/09/2022"
a = datetime.strptime(datar, "%d/%m/%Y")
b = datetime.strptime(datad, "%d/%m/%Y")
print(a)
print(b)
c = strptime(datar, "%d/%m/%Y")
d = strptime(datad, "%d/%m/%Y")






