import pandas as pd
from PySimpleGUI import PySimpleGUI as sg
import matplotlib.pyplot as plt

CACHE_FILE = "data_cache.csv"  # Nome do arquivo cache

def read_data():
    try:
        # Tenta ler os dados do arquivo cache
        data = pd.read_csv(CACHE_FILE, low_memory=False)
    except FileNotFoundError:
        # Se o arquivo de cache não existir, lê o arquivo excel e cria o arquivo cache
        data = pd.read_excel("base de dados - projeto big data.xlsx", index_col=False)
        data.to_csv(CACHE_FILE, index=False)
    return data

#Variaveis globais
Dados = read_data()
DataU = pd.to_datetime(Dados['Data'])
data = ()
Dado_usado = []

#Opções para os graficos
opcoes_P = ['Procedimento por ano', 'Procedimento por mês']

opcoes_B = ['Valor faturado por convênio e data', 'Quantidade de procedimentos realizados por convênio','Quantidade de procedimentos realizados por fornecedor']

opcoes_L = ['Total produzido por ano e por fornecedor']

#Funções
def grafico(p1):
    if p1 == 1:
        return 'pie'
    elif p1 == 2:
        return 'bar'
    else:
        return 'line'

def Escolha_tela1():
    valor = 0
    if valores['_GRA_1_'] == True:
        valor = 1
    elif valores['_GRA_2_'] == True:
        valor = 2
    elif valores['_GRA_3_'] == True:
        valor = 3
    return valor

def mostrar(lista):
    lista2 = []
    for i in range(len(lista)):
        lista2.append(lista[i])
    return lista2

def tela_inicial():
    sg.theme('LightGrey1')
    # sg.theme_previewer()

    layout = [
        [sg.Push(),
         sg.Text("Bem-vindo ao sistema Prático | Equipe de Anestesia", text_color="white", background_color="black",
                 font=("Arial", 14)), sg.Push()],
        [sg.Text("\n")],
        [sg.Push(), sg.Image(r'ea_logo.png'), sg.Push()],
        [sg.Text("\n")],
        [sg.Text("Escolha um tipo de grafico para analisar os seus dados: \n", font=("Arial", 12))],
        [sg.Radio("Gráfico em formato de Pizza", "RADIO", key='_GRA_1_')],
        [sg.Radio("Gráfico em formato de Barra", "RADIO", key='_GRA_2_')],
        [sg.Radio("Gráfico em formato de Linha", "RADIO", key='_GRA_3_')],
        [sg.Push(), sg.Button("Avançar", size=(10, 1), key='_AVANCAR_'), sg.Push()],
        [sg.Push(), sg.Button('Pesquisa em tabela', key='_TABELA_'), sg.Push()]
    ]
    return sg.Window('Sistema EA', layout=layout, finalize=True, size=(520, 510))

def tela_grafico(grafico):
    global data
    if (grafico == valores['_GRA_1_']):
        data = [[nome] for nome in opcoes_P]
    if (grafico == valores['_GRA_2_']):
        data = [[nome] for nome in opcoes_B]
    if (grafico == valores['_GRA_3_']):
        data = [[nome] for nome in opcoes_L]

    sg.theme('LightGrey1')

    layout = [
        [sg.Text("Escolhendo os dados", font=("Arial", 12), text_color="white", background_color="black")],
        [sg.Push(), sg.Image(r'ea_logo.png'), sg.Push()],
        [sg.Text("\n")],
        (sg.Table(values=data, headings=['Opçoes'], auto_size_columns=True, key='_ESCOLHA_TELA2_',
                  justification='left', expand_x=True),),
        [sg.Button('Ok', size=(10, 1), key='_OK_')],
        [sg.Button('Voltar', size=(10, 1), key='_VOLTAR_')],
        [sg.Button('Sair', size=(10, 1), key='_SAIR_')],
    ]

    return sg.Window('Sistema EA', layout=layout, finalize=True, size=(520, 510), element_justification='center')

def janela_escolha_Filtro():
    sg.theme('LightGrey1')
    layout = [
        [sg.Text("\n")],
        [sg.Push(), sg.Image(r'ea_logo.png'), sg.Push()],
        [sg.Text("\n")],
        [sg.Text('\n\nEscolha um topico: ', font=("Arial", 12))],
        [sg.Combo(list(Dados.columns), size=(20, 10), readonly=True, key='_ESCOLHA_', bind_return_key=True,
                  enable_events=True)],
        # [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
        [sg.Text('Quantidade de linhas no retorno: ', font=("Arial", 12))],
        [sg.Input(key='_QUANTIDADE_DE_LINHAS_', s=5, )],
        [sg.Button('Buscar 🔎', key='_puxar_dados_', size=(10, 1))],
        [sg.Button('Voltar', key='_GO_JANELA1_', size=(10, 1))]

    ]
    return sg.Window('Sistema EA', layout=layout, finalize=True, size=(520, 510), element_justification='center')

def janela_escolha_Fornecedor():
    janela2.hide()
    DadosOrdenados = Dados['Fornecedor']
    dados = list(DadosOrdenados.sort_values(ascending=True).unique())
    sg.theme('LightGrey1')
    layout = [
        [sg.Text("\n")],
        [sg.Push(), sg.Image(r'ea_logo.png'), sg.Push()],
        [sg.Text("\n")],
        [sg.Text('\n\nEscolha um Fornecedor: ', font=("Arial", 12))],
        [sg.Combo(values=dados, size=(20, 10), readonly=True, key='_FORNECEDOR_', bind_return_key=True,
                  enable_events=True)],
        # [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
        [sg.Button('Mostrar gráfico', key='_PUXAR_FORNECEDOR_', size=(10, 1))],
        [sg.Button('Voltar', key='_GO_JANELA31_', size=(10, 1))]

    ]
    return sg.Window('Sistema EA', layout=layout, finalize=True, size=(520, 510), element_justification='center')
def janela_amostra(l) -> object:
    data = [[nome] for nome in l]

    sg.theme('LightGrey1')
    layout = [
        [sg.Table(values=data, headings=[valores['_ESCOLHA_']], auto_size_columns=True, justification='left',
                  expand_x=True,
                  num_rows=25)],
        [sg.Button('Voltar', key='_GO_JANELA3_', size=(10, 1))],

    ]
    return sg.Window('Sistema EA', layout=layout, finalize=True, size=(520, 510))

#Definção de janelas
janela1, janela2, janela3, janela4, janela5 = tela_inicial(), None, None, None, None

#Inicio do programa
while True:
    window, eventos, valores = sg.read_all_windows()

    if eventos == sg.WIN_CLOSED or eventos == '_SAIR_':
        break
    # Tela de escolha do grafico
    if eventos == '_AVANCAR_':
        if (valores['_GRA_1_'] == True):
            janela1.hide()
            janela2 = tela_grafico(valores['_GRA_1_'])
            resp = 1
        elif (valores['_GRA_2_'] == True):
            janela1.hide()
            janela2 = tela_grafico(valores['_GRA_2_'])
            resp = 2
        elif (valores['_GRA_3_'] == True):
            janela1.hide()
            janela2 = tela_grafico(valores['_GRA_3_'])
            resp = 3
        else:
            sg.popup_ok('Por gentileza, Escolha um tipo de gráfico\n', title='Atenção')

    # Tela para filtro direto sem gráfico
    if eventos == '_TABELA_':
        janela1.hide()
        janela3 = janela_escolha_Filtro()

    if eventos == '_puxar_dados_' and valores['_QUANTIDADE_DE_LINHAS_'] != '' and valores['_ESCOLHA_'] != '':
        nd = valores['_ESCOLHA_']
        bd = Dados[nd]
        bd = bd.fillna('Não informado')
        # print(bd.head(10))
        # if window == janela1 and eventos == '_puxar_dados_':
        Dado_usado = bd.head(int(valores['_QUANTIDADE_DE_LINHAS_']))  # .tolist()
        # print(Dado_usado.values[3])
        Dado_usado = mostrar(Dado_usado.values)
        janela3.hide()
        janela4 = janela_amostra(Dado_usado)
        # print(Dado_usado) #resultado do filtro sem grafico

    # Botão voltar, tela resultado do filtro sem gráfico
    if eventos == '_GO_JANELA3_':
        janela4.hide()
        janela3 = janela_escolha_Filtro()

    # Botão voltar, tela escolha do filtro sem gráfico
    if eventos == '_GO_JANELA1_':
        janela3.hide()
        janela1 = tela_inicial()

    # Botão voltar, Para tela inicial
    if eventos == '_VOLTAR_':
        janela2.hide()
        janela1 = tela_inicial()

    if eventos == '_GO_JANELA31_':
        janela5.hide()
        janela2 = tela_inicial()

    # Tela para escolha do filtro com gráfico
    # Gráfico Pizza
    if eventos == '_OK_' and resp == 1:
        # procedimentos realizados por ano
        if valores['_ESCOLHA_TELA2_'] == [0]:
            Dados['Data'] = pd.to_datetime(Dados['Data'])
            agrupamento_ano = Dados.groupby(Dados['Data'].dt.year)['Procedimento realizado'].count().plot(
                kind='pie', autopct='%0.2f%%')
            # plt.title('Quantidade: ' + str(Dados['Data'].count()))
            plt.show()

        # procedimentos realizados por mês
        else:
            labels = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                      'Outubro', 'Novembro', 'Dezembro']
            Dados['Data'] = pd.to_datetime(Dados['Data'])
            agrupamento_mes = Dados.groupby(Dados['Data'].dt.month)['Procedimento realizado'].count().plot(
                labels=labels, kind='pie',
                autopct='%0.2f%%')
            # plt.legend(loc='right',title='Quantidade: ' + str(Dados['Data'].count()))
            plt.title('Quantidade: ' + str(Dados['Data'].count()))
            plt.show()
            # print(agrupamento_mes)

    # Gráfico Barra
    if eventos == '_OK_' and resp == 2:
        # Valor faturado por convênio e data
        if valores['_ESCOLHA_TELA2_'] == [0]:
            Dados['Data'] = pd.to_datetime(Dados['Data'])
            Dados['Data'] = Dados['Data'].dt.year
            Con_Dat = Dados.groupby(['Convenio', 'Data'])['Total Guia'].sum().unstack()
            Con_Dat.plot(kind='bar')

            # Configurando os rótulos dos eixos
            plt.xlabel('Data')
            plt.ylabel('Valor Faturado')

            # Exibindo o gráfico
            plt.legend(title=' Fatura Convênio DT')
            plt.show()

            # Quantidade de procedimentos realizados por convênio

        if valores['_ESCOLHA_TELA2_'] == [1]:
            Con__Qtd = Dados.groupby(['Convenio'])['Qtde'].sum()
            Con__Qtd.plot(kind='bar')

            # Configurando os rótulos dos eixos
            plt.xlabel('Convenio')
            plt.ylabel('Quantidade')

            # Exibindo o gráfico
            plt.legend(title=' Procedimento Realizado')
            plt.show()

        # Quantidade de procedimentos realizados por fornecedor
        else:
            Fat_Pro_For = Dados.groupby(['Fornecedor'])['Qtde'].sum()
            ax = Fat_Pro_For.plot(kind='bar', y='Qtde', x='Fornecedor')
            plt.legend(title=' Procedimento Realizado')
            ax.tick_params(axis='x', labelsize=4)
            plt.show()

        # Grafico Linha

    #Gráfico Linha
    if eventos == '_OK_' and resp == 3:
        # Total produzido por ano e por fornecedor
        if valores['_ESCOLHA_TELA2_'] == [0]:
            janela2.hide()
            janela5 = janela_escolha_Fornecedor()

    #continuação do grafico linha opção para escolha de fornecedor
    if eventos == '_PUXAR_FORNECEDOR_':
        fornecedor = valores['_FORNECEDOR_']
        Dados['Data'] = DataU
        Dados['Data'] = pd.to_datetime(Dados['Data'], format='YYYY')
        Dados['Data'] = Dados['Data'].dt.year
        Pro_For_Ano = Dados[Dados['Fornecedor'] == fornecedor]['Data'].value_counts().sort_index()
        Pro_For_Ano.plot(kind='line')
        plt.show()
        print(Pro_For_Ano.head(10))

window.close()