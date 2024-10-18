# abrir o excell

import pyautogui
import time
import pandas as pd

#pyautogui.PAUSE=0.5
pyautogui.press("win")
time.sleep(5)
pyautogui.write("excel")
pyautogui.press("enter")
time.sleep(5)
pyautogui.press("enter")


# importar os dados

tabela = pd.read_csv(r"C:\Formação Python Developer\Forma--o-Python-Developer\desafio_hashtag\produtos.csv")

for linha in tabela.index:
    # pegar da tabela o valor do campo que a gente quer preencher
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter")




pyautogui.write("PRONTO!!")
pyautogui.click(x=30, y=15)
time.sleep(3)
pyautogui.click(x=294, y=387)
time.sleep(3)
pyautogui.click(x=218, y=50)
time.sleep(3)
pyautogui.doubleClick(x=231, y=195)
time.sleep(3)
pyautogui.click(x=157, y=343)
time.sleep(3)
pyautogui.write("hashtag voando")
time.sleep(3)
pyautogui.press("enter")

