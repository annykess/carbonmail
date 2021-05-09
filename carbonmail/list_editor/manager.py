# Onde estarão todas as funções deste pacote.
# Ele é quem vai coordenar este pacote (gerenciador)


def initialize():
    from carbonmail.list_editor import List_Editor
    
    ems = List_Editor() 
    ems.enable_window()
    
