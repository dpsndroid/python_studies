# inside the package utilidadescev, in datas module, create a function called readmoney()
# like the function input(), but with data validation. To accept only monetary values

from uteis.utilitiescev import coin
from uteis.utilitiescev import data

n = data.read_money(str(input("type the price: R$ ")).lower().replace(",",".").strip())
ti = data.read_taxmajor(str(input("type the tax up: ")).lower().replace(",",".").strip())
td = data.read_taxminor(str(input("type the tax down: ")).lower().replace(",",".").strip())
coin.summary(n, ti, td)