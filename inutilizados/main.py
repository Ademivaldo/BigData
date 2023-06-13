import pandas as pd
from PySimpleGUI import PySimpleGUI as sg
import matplotlib.pyplot as plt

CACHE_FILE = "../data_cache.csv"  # Nome do arquivo cache

#produto = ["produto A","produto b","produto C","produto D","produto E"]
#vendas = [100,300,400,280,390]

def read_data():
    try:
        # Tenta ler os dados do arquivo cache
        data = pd.read_csv(CACHE_FILE, low_memory=False)
    except FileNotFoundError:
        # Se o arquivo cache não existir, lê o arquivo XLSX e cria o cache
        data = pd.read_excel("base de dados - projeto big data.xlsx", index_col=False)
        data.to_csv(CACHE_FILE, index=False)
    return data


Dados = read_data()
Dado_usado = []
def mostrar(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista[i])
    return lista2

def janela_escolha():
    sg.theme('dark Grey 13')
    layout = [
        [sg.Text('Escolha um topico : ')],
        [sg.Combo(list(Dados.columns), size=(20, 10), readonly=True, key='_ESCOLHA_', bind_return_key=True,
                  enable_events=True)],
        # [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
        [sg.Text('Quantidade de linhas \nno retorno')],
        [sg.Input(key='_QUANTIDADE_DE_LINHAS_',s=5)],
        [sg.Button('puxar', key='_puxar_dados_')]
    ]
    return sg.Window('Escolha de topico', layout=layout, finalize=True, size=(160, 260))


def janela_amostra(l) -> object:
    data = [[nome] for nome in l]

    sg.theme('dark Grey 13')
    layout = [
        [sg.Table(values=data ,headings=[valores['_ESCOLHA_']],auto_size_columns=True,justification='left' ,expand_x=True )],
        [sg.Button('Voltar',key='_GO_JANELA1_')]
    ]
    return sg.Window('Resultado', layout=layout, finalize=True, size=(400, 400))


janela1, janela2 = janela_escolha(), None

while True:

    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == '_puxar_dados_':
        nd = valores['_ESCOLHA_']
        bd = Dados[nd]
        bd = bd.fillna('Não informado')
        # print(bd.head(10))
        #if window == janela1 and eventos == '_puxar_dados_':
        Dado_usado = bd.head(int(valores['_QUANTIDADE_DE_LINHAS_'])) #.tolist()
        #print(Dado_usado.values[3])
        Dado_usado = mostrar(Dado_usado.values)
        janela2 = janela_amostra(Dado_usado)
        janela1.hide()
        print(Dado_usado)
    if window == janela2 and eventos == '_GO_JANELA1_':
        janela2.hide()
        janela1 = janela_escolha()

