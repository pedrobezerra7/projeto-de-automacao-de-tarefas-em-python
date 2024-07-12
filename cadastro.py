import pyautogui
import pandas
import time

# Abrir a interface gráfica
pyautogui.PAUSE = 0.30

pyautogui.press("win")
pyautogui.write("interface.exe")
pyautogui.press("enter")

time.sleep(5)

# Ler a planilha e preencher com os dados na interface gráfica
planilha = pandas.read_excel("clientes_ficticios.xlsx", header=0)

for cliente in planilha.index:
    # id
    pyautogui.click(736, 428)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    id = str(planilha.loc[cliente, "ID do Cliente"])
    pyautogui.write(id)

    # nome
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")    
    nome_sobrenome = str(planilha.loc[cliente, "Nome e Sobrenome"])
    pyautogui.write(nome_sobrenome)

    # endereço
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")    
    endereco = str(planilha.loc[cliente, "Endereço"])
    pyautogui.write(endereco)

    # cep
    pyautogui.press("tab")    
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")    
    cep = str(planilha.loc[cliente, "CEP"])
    pyautogui.write(cep)

    # uf
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")    
    uf = str(planilha.loc[cliente, "UF"])
    pyautogui.write(uf)

    # telefone
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")    
    telefone = str(planilha.loc[cliente, "Telefone"])
    pyautogui.write(telefone)

    # email
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")    
    email = str(planilha.loc[cliente, "E-mail"])
    pyautogui.write(email)
    
    pyautogui.click(1227, 762)
    pyautogui.click(964, 590)



