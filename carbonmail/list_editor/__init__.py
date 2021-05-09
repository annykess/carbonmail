# Arquivo usado para transformar a Pasta em Pacote
# Ele é sempre executado ao importar este pacote
# Arquivo usado para transformar a Pasta em Pacote
# Ele é sempre executado ao importar este pacote
import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.email_sender import view

class List_Editor():
    def __init__(self):
        self.window= None

    def instantiate(self):
        if self.window == None:
            self.window = view.get_window() 

    def enable_window(self):       

        self.instantiate()

        while True:
            event, values = self.window.read()

            if event == WIN_CLOSED:
                self.window.close()
                break
            if event == '-Send-':
                title= values['-Title-']
                content = values['-Content-']

                sg.Popup(
                    f" O titulo é: {title}\n O conteudo é: {content}",
                    title="E-mail",
                )

#fechar janela
    def close_window(self):
        if self.window  is not None:
            self.window.Close()
        

#ocultar janela
    def hide_window(self):
        if self.window  is not None:
            self.window.Hide()
        

#desocultar janela
    def unhide_window(self): 
        if self.window  is not None:
            self.window.UnHide()  
                            