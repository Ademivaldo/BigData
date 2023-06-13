import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])
        sg.popup('asdasdasdasdasd', title='Title')

window.close()

#import pandas as pd
from PySimpleGUI import PySimpleGUI as sg

CACHE_FILE = "../data_cache.csv"  # Nome do arquivo cache


#def read_data():
    #try:
        # Tenta ler os dados do arquivo cache
        #data = pd.read_csv(CACHE_FILE, low_memory=False)
        # except FileNotFoundError:
        # Se o arquivo cache não existir, lê o arquivo XLSX e cria o cache
        #data = pd.read_excel("base de dados - projeto big data.xlsx")
        #    data.to_csv(CACHE_FILE, index=False)
    #   return data


#Dados = read_data()
#sg.theme('reddit')

#layout = [
#   [sg.Text('user'), sg.Input(key='user')],
#   [sg.Text('senha'), sg.Input(key='senha', password_char='*')],
#   [sg.Checkbox('salvar?')],
#   [sg.Button('entrar',key='_puxar_dados_')]
#]

#janela = sg.Window('tela', layout)
#while True:
    #eventos, valores = janela.read()
    #   if eventos == sg.WIN_CLOSED:
#   break
    # if eventos == '_puxar_dados_':
        #Dados.info()
        #        print("alasd")


#para janela
#    menu_def = [['File', ['Open', 'Save', 'Exit',]],
#                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
#                ['Help', 'About...'],]
#




#import PySimpleGUIQt as sg

# Design pattern 1 - First window does not remain active

#layout = [[ sg.Text('Window 1'),],
#         [sg.Input(do_not_clear=True)],
#         [sg.Text(size=(15,1),  key='-OUTPUT-')],
#         [sg.Button('Launch 2')]]

#win1 = sg.Window('Window 1', layout)
#win2_active=False
#while True:
    #ev1, vals1 = win1.read(timeout=100)
    #   if ev1 == sg.WIN_CLOSED:
#   break
    #win1.FindElement('-OUTPUT-').update(vals1[0])

    #if ev1 == 'Launch 2'  and not win2_active:
        #win2_active = True
        #win1.Hide()
        #    layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
    #                   [sg.Button('Exit')]]

        #win2 = sg.Window('Window 2', layout2)
        #while True:
            #ev2, vals2 = win2.read()
            #if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                #win2.close()
                #                win2_active = False#
                #win1.UnHide()
#                break