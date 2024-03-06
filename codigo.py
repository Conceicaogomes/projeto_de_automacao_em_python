# Passo a passo do projeto:

# Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login


import pyautogui
import time 
pyautogui.PAUSE = 1

#abrindo o navegador chrome
pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

#entrando no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press('enter')

#dar uma pausa um pouco maior (3 segundos)
time.sleep(3)

# Fazendo login
pyautogui.click(x=655, y=298)
pyautogui.write("malkacanal@gmail.com")

#escrevendo a senha
pyautogui.press('tab')
pyautogui.write('senha aqui')

#clicando no botão de logar
pyautogui.click(x=715, y=416)
time.sleep(3)

# Importando a base de dados
import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Cadastrando 1 produto para cada linha da minha tabela

for linha in tabela.index:

    pyautogui.click(x=600, y=215)

    # codigo do produto
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # marca
    pyautogui.write(tabela.loc[linha,'marca'])
    pyautogui.press('tab')

    # tipo
    pyautogui.write(tabela.loc[linha,'tipo'])
    pyautogui.press('tab')

    # categoria
    pyautogui.write (str(tabela.loc[linha,'categoria']))
    pyautogui.press('tab')

    # preco_unitario
    pyautogui.write (str(tabela.loc[linha,'preco_unitario']))
    pyautogui.press('tab')

    # custo
    pyautogui.write (str(tabela.loc[linha,'custo']))
    pyautogui.press('tab')

    # obs
    obs= tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
    
        pyautogui.write(obs)
    pyautogui.press('tab')

    #enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)

# Final - Repetir o processo de cadastro até acabar a base de dados
