#onde fica o codigo para interface grafica
#tudo que servir de visual fica aqui
# É principalmente aqui que usaremos o PySimpleGUI
import PySimpleGUI as sg 

#window => janela
#Layout => oq que vai mostrar na janela
#        =>=> Lista de Listas
#             Cada sublista é uma "Linha" da Janela
#             Cada elemento é um componente visual

lista = ['Administradores','Alunos']

def get_layout():
    layout = [
        [sg.Text('Selecione o seu código'),
        sg.In(),
        sg.FileBrowse('Selecione', file_types =( ("Códigos Python", "*.py*"), )),
        ],
        [
            sg.Text('Selecione a lista de destinatario'),
            sg.Combo(lista, default_value = lista[1]),
        ],
        [
            sg.Text('Insira o Titulo: '),
            sg.In(key='-Title-'),
        ],
        [
            sg.Text('Insira o conteudo do E-mail: '),
            sg.MLine(key='-Content-')            
        ],
        [
            sg.Button('Enviar', key='-Send-'),
            sg.Button('Gerenciar Listas', key='-ListEditor-'),
        ],

    ]

    return layout

def get_window():
    return sg.Window('Teste de janela', get_layout())
