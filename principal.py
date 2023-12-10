from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from email_thread import EmailThread
from main_ui import Ui_MainWindow
import sys
import re
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("BruTha - Envio de E-mail")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
        self.init_banco_dados()
        self.carregar_dados_tabela()
        # Conectar sinais e slots
        self.btn_menu.clicked.connect(self.menu_lateral)
        self.btn_corpo.setEnabled(False)
        self.btn_enviar.setEnabled(False)
        self.btn_config.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_usuario))
        self.btn_adicionar.clicked.connect(self.update_button_state)
        self.btn_corpo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_corpo))
        self.btn_menu.clicked.connect(self.carregar_dados_tabela)
        self.btn_menu.clicked.connect(self.update_button_state)
        self.btn_excluir_2.clicked.connect(self.excluir_desti)
        self.btn_enviar.clicked.connect(self.enviar_se)
        self.btn_adicionar.clicked.connect(self.add_tabela)
        self.btn_anexo.clicked.connect(self.carregar_arquivo)
        self.barra_deprogresso.setValue(0)

        # Inicializar thread para enviar e-mails
        self.email_thread = EmailThread()
        self.email_thread.progress_signal.connect(self.atualizar_progresso)

    def init_banco_dados(self):
        try:
            self.conexao = sqlite3.connect('cadastro.db')
            self.cursor = self.conexao.cursor()
            self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS usuarios (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT,
                            funcao TEXT
                        )
                    ''')
            self.conexao.commit()
            self.carregar_dados_tabela()
            self.update_button_state()

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Erro no Banco de Dados", f"Erro ao inicializar o banco de dados: {str(e)}")
            sys.exit()

    def carregar_dados_tabela(self):
        self.tableWidget_2.setRowCount(0)
        try:
            self.cursor.execute('SELECT email, funcao FROM usuarios')
            dados = self.cursor.fetchall()

            for row_num, row_data in enumerate(dados):
                self.tableWidget_2.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    self.tableWidget_2.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

        except sqlite3.Error as e:
            if "no such table: usuarios" in str(e):
                self.init_banco_dados()
                self.carregar_dados_tabela()
            else:
                QMessageBox.critical(self, "Erro no Banco de Dados", f"Erro ao carregar dados da tabela: {str(e)}")

    def is_table_empty(self):
        return self.tableWidget_2.rowCount() == 0

    def update_button_state(self):
        self.btn_corpo.setEnabled(not self.is_table_empty())

    def enviar_se(self):
        self.barra_deprogresso.setValue(0)
        corpo = self.txt_corpo.toPlainText()
        arquivo_anexo = self.lineEdit.text()

        if corpo != "" and arquivo_anexo:
            self.enviar_email(corpo, arquivo_anexo)
            self.email_thread.progress_signal2.connect(self.atualizar_barra_progresso)
            self.email_thread.start()
        elif not arquivo_anexo:
            QMessageBox.critical(self, "Arquivo não selecionado - Campos vazios",
                                 "Selecione um arquivo / Preencha o corpo do e-mail")
        else:
            QMessageBox.critical(self, "Corpo de mensagem vazio", "Favor inserir informações")

    def atualizar_barra_progresso(self, progresso):
        if progresso >= 0:
            self.barra_deprogresso.setValue(progresso)
        else:
            # QMessageBox.critical(self, "Erro ao enviar e-mail", "Ocorreu um erro durante o envio de e-mails.")
            self.barra_deprogresso.setValue(0)

    def carregar_arquivo(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly
        arquivo, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Carregar Arquivo", "",
                                                           "Todos os Arquivos (*);;Text Files (*.txt)", options=options)

        if arquivo:
            self.lineEdit.setText(arquivo)
            self.btn_enviar.setEnabled(True)
        return None

    @staticmethod
    def verifi_e_mail(emaill):
        email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return re.match(email_regex, emaill)

    def excluir_desti(self):
        selected_rows = set(index.row() for index in self.tableWidget_2.selectedIndexes())

        if selected_rows:
            try:
                for row_num in sorted(selected_rows, reverse=True):
                    email = self.tableWidget_2.item(row_num, 0).text()
                    self.cursor.execute('DELETE FROM usuarios WHERE email = ?', (email,))
                    self.tableWidget_2.removeRow(row_num)

                self.conexao.commit()
                self.update_button_state()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Erro no Banco de Dados", f"Erro ao excluir registros: {str(e)}")
        else:
            QMessageBox.critical(self, "Erro", "Nenhum registro selecionado para exclusão.")

    def add_tabela(self):
        email1 = self.txt_email.text()
        email2 = self.txt_destino.text()
        funcao = self.txt_funcao.text()
        senha = self.txt_senha.text()

        if self.verifi_e_mail(email1) and self.verifi_e_mail(email2):
            if email2 != "" and funcao != "" and email1 != "" and senha != "":
                try:
                    posicao = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(posicao)
                    self.tableWidget_2.setItem(posicao, 0, QTableWidgetItem(email2))
                    self.tableWidget_2.setItem(posicao, 1, QTableWidgetItem(funcao))

                    self.cursor.execute('INSERT INTO usuarios (email, funcao) VALUES (?, ?)', (email2, funcao))
                    self.conexao.commit()
                    self.carregar_dados_tabela()

                    self.txt_destino.clear()
                    self.txt_funcao.clear()

                except sqlite3.Error as e:
                    QMessageBox.critical(self, "Erro no Banco de Dados", f"Erro ao adicionar dados à tabela: {str(e)}")
            else:
                QMessageBox.about(self, "Cadastro", "Informar todos os dados")
        else:
            QMessageBox.about(self, "E-mail", "Corrija o(s) E-mail(s) digitados.")
        self.update_button_state()

    def enviar_email(self, corpo, arquivo_anexo):
        meuemail = self.txt_email.text()
        senha = self.txt_senha.text()
        self.txt_progresso.clear()

        row_data_list = []

        for row_num in range(self.tableWidget_2.rowCount()):
            email = self.tableWidget_2.item(row_num, 0).text()
            assunto_personalizado = self.tableWidget_2.item(row_num, 1).text()

            row_data_list.append((email, assunto_personalizado, corpo))

        # Parar a thread anterior, se estiver em execução
        if self.email_thread.isRunning():
            self.email_thread.stop()
            self.email_thread.wait()

        # Iniciar nova thread para enviar e-mails
        self.email_thread.set_data(meuemail, senha, row_data_list, arquivo_anexo)
        self.email_thread.start()

    def atualizar_progresso(self, mensagem):
        self.txt_progresso.insertPlainText(mensagem)
        cursor = self.txt_progresso.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.txt_progresso.setTextCursor(cursor)

    def menu_lateral(self):
        width = self.frame_lateral.width()
        if width == 0:
            newWidth = 120
        else:
            newWidth = 0
            self.stackedWidget.setCurrentWidget(self.inicial)
        self.animation = QtCore.QPropertyAnimation(self.frame_lateral, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def menu_lateral_inicial(self):
        width = self.frame_lateral.width()
        if width == 0:
            newWidth = 120
        else:
            newWidth = 0
            self.stackedWidget.setCurrentWidget(self.inicial)
        self.animation = QtCore.QPropertyAnimation(self.frame_lateral, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def update_button_state(self):
        has_data = not self.is_table_empty()
        self.btn_corpo.setEnabled(has_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
