#################################################################################################################################################
LEMBRANDO QUE PARA ACESSAR O SISTEMA A SENHA DE APLICATIVO DE TERCEIROS DEVE ESTAR CONFIGURADA NAS CONFIG DO SEU G-MAIL.
ESTANDO COM ESSA SENHA NÃO TERA DIFUCLDADES.
#################################################################################################################################################



#Título do Projeto: BruTha - Envio de E-mail

#Linguagem Utilizada: Python com PySide6 (Qt) para a interface gráfica

Descrição:
Este projeto consiste em uma aplicação de envio de e-mails com interface gráfica utilizando PySide6 (Qt). O código principal, principal.py, é uma implementação de uma interface de usuário usando o Qt Designer (main_ui.ui). O programa permite o cadastro de destinatários, envio de e-mails com anexos e exibição de progresso em uma barra de progresso.

#Recursos Principais:

#Interface gráfica criada com Qt Designer.
#Utilização de SQLite para armazenar informações de usuários.
#Threading para evitar travamento da interface durante o envio de e-mails em segundo plano.
#Validação de e-mails e tratamento de erros durante o envio.
Arquivos Principais:

#principal.py: Contém a classe principal da aplicação, que herda de QMainWindow. Gerencia a interface gráfica, interação com o banco de dados SQLite, e envio de e-mails.
#main_ui.ui: Arquivo XML gerado pelo Qt Designer, contendo a descrição da interface gráfica.
email_thread.py: Contém a implementação de uma thread (EmailThread) para enviar e-mails em segundo plano, permitindo que a interface permaneça responsiva durante o processo.
Funcionalidades Principais:

Cadastro de usuários (destinatários) com e-mails e funções.
Envio de e-mails personalizados para os destinatários cadastrados.
Anexo de arquivos aos e-mails.
Barra de progresso para acompanhar o status do envio.
Como Executar:

Execute principal.py para iniciar a aplicação.
Cadastre os destinatários na interface.
Preencha o corpo do e-mail e selecione um arquivo para anexo.
Clique no botão "Enviar" para iniciar o processo de envio.
A barra de progresso exibe o status do envio.
Mensagens de sucesso ou erro são exibidas na área de progresso.
Observações:

O projeto utiliza SQLite para armazenar dados localmente.
A aplicação realiza a validação de e-mails e trata diferentes cenários de erro durante o envio.
Requisitos:

Python 3.x
PySide6
Este projeto é uma ferramenta útil para quem precisa enviar e-mails para múltiplos destinatários de forma automatizada, mantendo uma interface amigável e responsiva durante o processo.


![Captura de tela de 2023-12-10 12-45-17](https://github.com/Bruno-Luiz-CNR/Envio-de-E-MAIL/assets/115126390/bc30b967-acaa-44bd-92b2-0fc5a3e2496f)
![Captura de tela de 2023-12-10 12-45-28](https://github.com/Bruno-Luiz-CNR/Envio-de-E-MAIL/assets/115126390/9969c3b7-b506-462d-8dd8-3ffe38eeed6f)
![Captura de tela de 2023-12-10 12-45-59](https://github.com/Bruno-Luiz-CNR/Envio-de-E-MAIL/assets/115126390/eb7db297-23c6-40d3-a8bb-ab8a18bc640b)

