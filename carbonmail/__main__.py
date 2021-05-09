#Arquivo principal a ser executado
#quando iniciamos o projeto (carbonmail) ele é o primeiro a ser executado
#nós usamos para ser  o ponto de entrada da aplicacao
from carbonmail.email_sender.manager import initialize as init_sender

init_sender()
