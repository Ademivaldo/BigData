import pandas as pd
from PySimpleGUI import PySimpleGUI as sg
import matplotlib.pyplot as plt
import plotly.express as px


CACHE_FILE = "../data_cache.csv"  # Nome do arquivo cache


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

opcoes = ['Procedimento por ano','Procedimento por mês','Valor faturado por convênio e data',
          'Quantidade de procedimentos realizados por convênio',#'Quantidade de procedimentos e valor faturado',
          'Valor faturado e quantidade de procedimentos realizados por fornecedor','Total produzido por ano e por fornecedor']



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



def tela_inicial():
    sg.theme('dark Grey 13')

    layout = [
        [sg.Text("Escolha o tipo de grafico: ")],
        [sg.Radio("Pizza", "RADIO", key='_GRA_1_')],
        [sg.Radio("Coluna", "RADIO", key='_GRA_2_')],
        [sg.Radio("Linha", "RADIO", key='_GRA_3_')],
        [sg.Button("Avançar", key='_AVANCAR_')]
    ]
    return sg.Window('Resultado', layout=layout, finalize=True, size=(400, 400), )

def tela_grafico():


    data = [[nome] for nome in opcoes]
    sg.theme('dark grey 12')

    layout = [
        [sg.Text("Escolhendo os dados ")],
        [sg.Table(values=data,headings=['Opçoes'], auto_size_columns=True, key='_ESCOLHA_TELA2_',
                  justification='left' ,expand_x=True)],
        [sg.Button('Ok', key='_OK_')],
        [sg.Button('Voltar', key='_VOLTAR_')],
        [sg.Button('Sair', key='_SAIR_')],



    ]
    return sg.Window('Grafico', layout=layout, finalize=True, size=(520, 510), element_justification='center')


janela1, janela2 = tela_inicial(), None



while True:
    window, eventos, valores = sg.read_all_windows()

    if eventos == sg.WIN_CLOSED or eventos == '_SAIR_':
        break
    if eventos == '_AVANCAR_':
        janela1.hide()
        janela2 = tela_grafico()
        resp = [valores['_GRA_1_'],valores['_GRA_2_'],valores['_GRA_3_']]


    if  eventos == '_OK_' and resp[0] == True:
        if valores['_ESCOLHA_TELA2_'] == [0]:
            Dados['Data'] = pd.to_datetime(Dados['Data'])
            agrupamento_ano = Dados.groupby(Dados['Data'].dt.year)['Procedimento realizado'].count().plot(
                   kind='pie', autopct='%0.2f%%')
            plt.title('Quantidade: ' + str(Dados['Data'].count()))
            plt.show()

        elif valores['_ESCOLHA_TELA2_'] == [1]:
            labels = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
            Dados['Data'] = pd.to_datetime(Dados['Data'])
            agrupamento_mes = Dados.groupby(Dados['Data'].dt.month)['Procedimento realizado'].count().plot(
                kind='pie', autopct='%0.2f%%')
            plt.legend( loc='right',title='Quantidade: ' + str(Dados['Data'].count()))
            plt.title('Quantidade: ' + str(Dados['Data'].count()))
            plt.show()
            #print(agrupamento_mes)

        elif valores['_ESCOLHA_TELA2_'] == [3]:
            Dados = Dados.groupby(Dados['Convenio'])['Procedimento realizado'].count()
            Dados.plot(
                kind='pie', autopct='%0.2f%%')
            plt.show()

        elif valores['_ESCOLHA_TELA2_'] == [4]:
            # Dados = Dados.fillna('Não informado')
            # Dados = Dados.groupby(Dados['Fornecedor'])['Total Guia'].value_counts()
            # print(Dados.head(20))
            # Dados.plot(
            #      kind='pie', autopct='%0.2f%%')
            # #plt.show()
            # print(Dados.head())
            Dados['Data'] = pd.to_datetime(Dados['Data'])
            Dados['Ano'] = Dados['Data'].dt.year

            Fornecedor_Ano = Dados.groupby('Fornecedor')['Total Guia'].sum()

            plt.figure()
            plt.pie(Fornecedor_Ano, labels=Fornecedor_Ano.index, autopct='%1.1f%%')
            plt.title('Total de fornecedores por data (Todos os anos)')
            plt.axis('equal')
            plt.show()

        elif valores['_ESCOLHA_TELA2_'] == [5]:
            Dados['Data'] = pd.to_datetime(Dados['Data'])
            Dados['Ano'] = Dados['Data'].dt.year

            df_grouped = Dados.groupby(['Ano', 'Fornecedor'])['Total Guia'].sum().reset_index()

            #plt.figure(figsize=(8, 6))

            for ano in df_grouped['Ano'].unique():
                df_ano = df_grouped[df_grouped['Ano'] == ano]
                plt.pie(df_ano['Total Guia'], labels=df_ano['Fornecedor'], autopct='%1.0f%%', startangle=90)
                plt.title(f'Total Produzido por Fornecedor - Ano {ano}')
                plt.axis('equal')
                plt.show()
            ##############################################################################################



    # if eventos == '_OK_' and resp[1] == True:
    #     if valores['_ESCOLHA_TELA2_'] == [0]:
    #         Dados['Data'] = pd.to_datetime(Dados['Data'])
    #         agrupamento_ano = Dados.groupby(Dados['Data'].dt.year)['Procedimento realizado'].count().plot(
    #             kind='bar')
    #         plt.show()
    #     if valores['_ESCOLHA_TELA2_'] == [1]:
    #         Dados['Data'] = pd.to_datetime(Dados['Data'])
    #         agrupamento_mes = Dados.groupby(Dados['Data'].dt.month)['Procedimento realizado'].count().plot(
    #             kind='bar')
    #         # plt.legend( loc='right',title='Quantidade: ' + str(Dados['Data'].count()))
    #         plt.title('Quantidade: ' + str(Dados['Data'].count()))
    #         plt.show()
    #
    #     if valores['_ESCOLHA_TELA2_'] == [2]:
    #         elif valores['_ESCOLHA_TELA2_'] == [2]:
    #         # Agrupando os valores por convênio e data e somando os valores faturados
    #         Dados['Data'] = pd.to_datetime(Dados['Data'])
    #         Dados['Data'] = Dados['Data'].dt.year
    #         df_agrupado = Dados.groupby(['Convenio', 'Data'])['Total Guia'].sum().unstack()
    #
    #         # Plotando o gráfico de barras empilhadas
    #         df_agrupado.plot(kind='bar')
    #
    #         # Configurando os rótulos dos eixos
    #         plt.xlabel('Data')
    #         plt.ylabel('Valor Faturado')
    #
    #         # Exibindo o gráfico
    #         # plt.legend(title='Convênio')
    #         plt.show()
    #
    # if eventos == '_OK_' and resp[2] == True:
    #     if valores['_ESCOLHA_TELA2_'] == [0]:
    #         Dados['Data'] = pd.to_datetime(Dados['Data'])
    #         agrupamento_ano = Dados.groupby(Dados['Data'].dt.year)['Procedimento realizado'].count().plot(
    #             kind='line')
    #         plt.show()
    #     if valores['_ESCOLHA_TELA2_'] == [1]:
    #         Dados['Data'] = pd.to_datetime(Dados['Data'])
    #         agrupamento_mes = Dados.groupby(Dados['Data'].dt.month)['Procedimento realizado'].count().plot(
    #             kind='line')
    #         # plt.legend( loc='right',title='Quantidade: ' + str(Dados['Data'].count()))
    #         plt.title('Quantidade: ' + str(Dados['Data'].count()))
    #         plt.show()

    if eventos == '_VOLTAR_':
        janela2.hide()
        janela1 = tela_inicial()



window.close()

# print(agrupamento_ano)
# Dadostemp = Dados[['Data','Procedimento realizado']]
# cont = Dados['Procedimento realizado'].count()
# fig, ax = plt.subplots()
# ax.bar(Dadostemp['Data'], 1000)
# ax.set(title="Lista de produtos", ylabel="Preço");

# print(Dadostemp.head())


#best
#upper
#right
#upper
#left
#lower
#left
#lower
#right
#right
#center
#left
#center
#right
#lower
#center
#upper
#center
#center