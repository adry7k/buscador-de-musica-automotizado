#Buscador de musica automotizado
import pyautogui
import time
def buscador():          
    print("Qual musica você está procurando?")
    nome_da_banda_ou_musico = input("Informe o nome da banda/cantor(a):")
    nome_da_musica = input("Informe o nome da musica:")
    return nome_da_banda_ou_musico, nome_da_musica

nome_da_banda_ou_musico, nome_da_musica = buscador()
busca = f"{nome_da_banda_ou_musico} - {nome_da_musica}"
print(busca)

time.sleep(2)
pyautogui.PAUSE = 0.8
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=425, y=904)
pyautogui.write(busca)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=550, y=568,clicks=2)






