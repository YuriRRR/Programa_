import pyautogui
from time import sleep
# 1 - EXTRAIR CADA PRODUTO
with open('registros_ficticios.csv', 'r' ) as arquivo:
    for linha in arquivo:
        nome = linha.split(',')[0]
        cidade = linha.split(',')[1]
        email = linha.split(',')[2]
        telefone = linha.split(',')[3]
        idade = linha.split(',')[4]
        # 2 - CLICAR E REGISTRAR NOME
        pyautogui.click(775,427,duration=0.1)
        pyautogui.write(nome)
        # 3 - CLICAR E REGISTRAR CIDADE
        pyautogui.click(777,457,duration=0.1)
        pyautogui.write(cidade)
        # 4 - CLICAR E REGISTRAR EMAIL
        pyautogui.click(776,498,duration=0.1)
        pyautogui.write(email)
        # 5 - CLICAR E REGISTRAR TELEFONE
        pyautogui.click(779,531,duration=0.1)
        pyautogui.write(telefone)
        # 7 - CLICAR E REGISTRAR IDADE
        pyautogui.click(782,561,duration=0.1)
        pyautogui.write(idade)
        # 6 - CLICAR EM CONFIRMAR
        pyautogui.click(788,714,duration=0.1)
        # 8 - CLICAR NO OK
        pyautogui.click(1025, 588, duration=0.1)
# 9 - ESPERAR 1 SEGUNDO ANTES DE INICIAR O PRÓXIMO REGISTRO
sleep(1)