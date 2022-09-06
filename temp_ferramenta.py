# controle de tempo de aluguel da ferramenta

from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta

ano = 2022
mes = int(input("mes: "))
dia = int(input("dia: "))
hora = int(input("hora: "))
          

data2 = datetime(year=2022, month=mes, day=dia, hour=hora, minute=00, second=00)
print(f"Data e hora de retirada: {data2}")

delta = relativedelta(hours=+8)
result = data2 + delta
print(f"Data e hora de devolução: {result}")





