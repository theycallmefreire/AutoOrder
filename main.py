import pyautogui as pa
import time 
pa.PAUSE = 1

# login
pa.press('win')
pa.write('chrome')
pa.press('ENTER')
#garantindo que a tena vai estar em tela cheia
time.sleep(2)
pa.hotkey('alt', 'space')
time.sleep(0.5)
pa.press('x')
pa.write('https://pium.7focus.inf.br/pium/#/index')#esconder essa info dps
pa.press('ENTER')
pa.click(x=752, y=574)#SELECIONAR COMPRAS  
pa.click(x=914, y=439)#selecionar saude
pa.click(x=877, y=598)
pa.click(x=785, y=841) # entrar
pa.click(x=1018, y=478)#entra em licitações
pa.sleep(2)
pa.doubleClick(x=376, y=438)#entra na adesao de ata
pa.sleep(2)
pa.click(x=191, y=604)#entrar em preços
pa.click(x=492, y=419)#pesquisar item

for i in range(1, n):#loop para inserir n itens
pa.write(item)#escrever item
pa.press('ENTER')

#[...]
pa.click(x=1888, y=29)#fechar janela



# entrar no sistema correto
# inserir lista de itens em loop
