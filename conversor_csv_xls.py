import openpyxl
import pandas as pd
import os
from datetime import date, time, datetime, timedelta
import pathlib


def exportxls():
    hoje = datetime.now()
    aa = str(hoje)
    bb = aa.split(" ")
    cc = bb[0]
    dd = bb[1]
    ee = dd.split(":")
    print(ee)
    h = ee[0]
    m = ee[1]
    ff = f"{h}-{m}"
    print(ff)
    novo = f"tecnico{cc}-{ff}hs.xlsx"
    print(novo)
    caminho = os.path.abspath(os.getcwd())
    print(caminho)
    print(type(caminho))
    cam = caminho.replace("\\","/")
    cam2 = f"{cam}/"

    print("oi")
    print(cam2)
    print(os.path.dirname(os.path.realpath(novo)))

    arquivo = pd.read_csv("tecnico.csv")
    arquivo.to_excel("tecnico.xlsx", sheet_name="Testing", index=False)

    os.rename("tecnico.xlsx", novo)
    
    file_source = cam2
    file_destination = 'c:/Users/Public/Downloads/'
    file_destination2 = '/home/'
    
    g = novo

    try:
        os.replace(file_source + g, file_destination2 + g)
    except:
        os.replace(file_source + g, file_destination + g)