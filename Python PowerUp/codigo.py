import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=1163, y=376) # posição considerando o tamanho do monitor
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=1101, y=241)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":    
        pyautogui.write(obs)    
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)