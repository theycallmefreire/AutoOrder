import pyautogui as pa
import time 
import pandas as pd
import unicodedata


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
pa.sleep(4)
pa.click(x=752, y=574)#SELECIONAR COMPRAS
pa.sleep(2)  
pa.click(x=914, y=439)#selecionar saude
pa.click(x=877, y=598)
pa.click(x=785, y=841) # entrar
pa.sleep(2)
pa.click(x=1018, y=478)#entra em licitações
pa.sleep(2)
pa.doubleClick(x=376, y=438)#entra na adesao de ata
pa.sleep(2)
pa.click(x=191, y=604)#entrar em preços
pa.sleep(2)

def remover_acentos(texto):
    if not isinstance(texto, str):
        return texto
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

arquivo = 'lista_hpp.xlsx'



df = pd.read_excel(arquivo)
df.columns = df.columns.str.strip()  # limpa espaços extras nos nomes das colunas




quantidade = df['DESCRIÇÃO DO ITEM'].count()

df['DESCRIÇÃO DO ITEM'] = df['DESCRIÇÃO DO ITEM'].apply(remover_acentos)

# Faz loop para cada item da coluna
for i in range(quantidade):  # ou: for item in df['DESCRIÇÃO DO ITEM'].dropna():
    item = df['DESCRIÇÃO DO ITEM'][i]
    qtde = df['QTDE'][i]
    qtde_formatado = f"{qtde:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    Valor= df['Valor Unitário'][i]
    # Remove "R$", espaços e substitui vírgula por ponto para converter
    valor_limpo = str(Valor).replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
    try:
        valor_num = float(valor_limpo)
        valor_formatado = f"{valor_num:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except ValueError:
        print(f"Valor inválido na linha {i}: {Valor}")
        valor_formatado = "0,00"

    print(f"Inserindo item {i}: {item}")
    pa.click(x=574, y=419)
    pa.hotkey('ctrl', 'a')
    pa.press('backspace')
    pa.write(str(item)[:7])
    pa.press('ENTER')
    time.sleep(2)
    pa.click(x=378, y=603)
    pa.sleep(2)
    pa.click(x=707, y=750)
    pa.hotkey('ctrl', 'a')
    pa.press('backspace')
    pa.write(str(qtde_formatado))
    pa.press('tab')
    pa.write(str(valor_formatado))
    pa.click(x=418, y=412)
    pa.sleep(2)

print("Todos os itens foram inseridos com sucesso!")
pa.sleep(2)
#[...]
pa.click(x=1888, y=29)#fechar janela



