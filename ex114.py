# Create a python code that tests if the website
# pudim is accessible

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site pudim não está acessível no momento")
else:
    print("Consegui acessar o site pudim com sucesso")
    print(site.read())