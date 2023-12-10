# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPlainTextEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import pic_qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(985, 692)
        MainWindow.setMinimumSize(QSize(985, 692))
        MainWindow.setMaximumSize(QSize(985, 692))
        font = QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"pic/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setFont(font)
        self.frame_superior.setAutoFillBackground(False)
        self.frame_superior.setStyleSheet(u"background-color: rgb(10, 27, 57);\n"
"image: url(:/pic_qt/cima.png);")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.frame_superior.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 9, 0)
        self.btn_menu = QPushButton(self.frame_superior)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setAutoFillBackground(False)
        self.btn_menu.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(5, 9, 67);\n"
"	image:rgb(5, 9, 67);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(97, 53, 131);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"pic/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon1)
        self.btn_menu.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.horizontalSpacer = QSpacerItem(418, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_enviar = QPushButton(self.frame_superior)
        self.btn_enviar.setObjectName(u"btn_enviar")
        self.btn_enviar.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setPointSize(14)
        self.btn_enviar.setFont(font1)
        self.btn_enviar.setAutoFillBackground(False)
        self.btn_enviar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(5, 9, 67);\n"
"	image:rgb(5, 9, 67);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(97, 53, 131);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"pic/enviar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_enviar.setIcon(icon2)
        self.btn_enviar.setIconSize(QSize(32, 28))
        self.btn_enviar.setFlat(False)

        self.horizontalLayout_2.addWidget(self.btn_enviar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setStyleSheet(u"\n"
"image: url(:/pic_qt/lateral.png);")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 0)
        self.btn_config = QPushButton(self.frame_lateral)
        self.btn_config.setObjectName(u"btn_config")
        font2 = QFont()
        font2.setPointSize(13)
        self.btn_config.setFont(font2)
        self.btn_config.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(5, 9, 67);\n"
"	image:rgb(5, 9, 67);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(97, 53, 131);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.btn_config.setIcon(icon)
        self.btn_config.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_config)

        self.btn_corpo = QPushButton(self.frame_lateral)
        self.btn_corpo.setObjectName(u"btn_corpo")
        self.btn_corpo.setFont(font1)
        self.btn_corpo.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color:rgb(5, 9, 67);\n"
"	image:rgb(5, 9, 67);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(97, 53, 131);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"pic/corpo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_corpo.setIcon(icon3)
        self.btn_corpo.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btn_corpo)

        self.verticalSpacer = QSpacerItem(20, 276, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_lateral)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Z003"])
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setItalic(True)
        self.label.setFont(font3)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"image:none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.btn_corpo.raise_()
        self.btn_config.raise_()
        self.label.raise_()

        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_centro = QFrame(self.frame_inferior)
        self.frame_centro.setObjectName(u"frame_centro")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_centro.sizePolicy().hasHeightForWidth())
        self.frame_centro.setSizePolicy(sizePolicy)
        self.frame_centro.setStyleSheet(u"")
        self.frame_centro.setFrameShape(QFrame.StyledPanel)
        self.frame_centro.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_centro)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_centro)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(5, 9, 67);\n"
"")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.inicial = QWidget()
        self.inicial.setObjectName(u"inicial")
        self.inicial.setStyleSheet(u"background-image: url(:/pic_qt/e-mail.png);")
        self.stackedWidget.addWidget(self.inicial)
        self.pg_usuario = QWidget()
        self.pg_usuario.setObjectName(u"pg_usuario")
        self.pg_usuario.setStyleSheet(u"image: url(:/pic_qt/centro.png);")
        self.btn_adicionar = QPushButton(self.pg_usuario)
        self.btn_adicionar.setObjectName(u"btn_adicionar")
        self.btn_adicionar.setEnabled(True)
        self.btn_adicionar.setGeometry(QRect(600, 110, 111, 31))
        font4 = QFont()
        font4.setStyleStrategy(QFont.PreferDefault)
        self.btn_adicionar.setFont(font4)
        self.btn_adicionar.setLayoutDirection(Qt.LeftToRight)
        self.btn_adicionar.setAutoFillBackground(False)
        self.btn_adicionar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(94, 92, 100);\n"
"	image:rgb(94, 92, 100);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(97, 53, 131);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"pic/adcemail.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adicionar.setIcon(icon4)
        self.btn_adicionar.setIconSize(QSize(28, 28))
        self.btn_adicionar.setAutoDefault(True)
        self.btn_adicionar.setFlat(False)
        self.txt_destino = QLineEdit(self.pg_usuario)
        self.txt_destino.setObjectName(u"txt_destino")
        self.txt_destino.setGeometry(QRect(20, 120, 311, 25))
        self.txt_destino.setFocusPolicy(Qt.ClickFocus)
        self.txt_destino.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.txt_destino.setAcceptDrops(True)
        self.txt_destino.setAutoFillBackground(False)
        self.txt_destino.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(61, 56, 70);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(154, 153, 150);\n"
"}")
        self.txt_funcao = QLineEdit(self.pg_usuario)
        self.txt_funcao.setObjectName(u"txt_funcao")
        self.txt_funcao.setGeometry(QRect(350, 120, 231, 25))
        self.txt_funcao.setFocusPolicy(Qt.ClickFocus)
        self.txt_funcao.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.txt_funcao.setAcceptDrops(True)
        self.txt_funcao.setAutoFillBackground(False)
        self.txt_funcao.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(61, 56, 70);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(154, 153, 150);\n"
"}")
        self.btn_excluir_2 = QPushButton(self.pg_usuario)
        self.btn_excluir_2.setObjectName(u"btn_excluir_2")
        self.btn_excluir_2.setGeometry(QRect(740, 110, 111, 31))
        self.btn_excluir_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(94, 92, 100);\n"
"	image:rgb(94, 92, 100);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(97, 53, 131);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"pic/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir_2.setIcon(icon5)
        self.btn_excluir_2.setIconSize(QSize(28, 28))
        self.tableWidget_2 = QTableWidget(self.pg_usuario)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        icon6 = QIcon()
        icon6.addFile(u":/pic_qt/corpo.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon6);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon7 = QIcon()
        icon7.addFile(u":/pic_qt/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setIcon(icon7);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 150, 831, 481))
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(94, 92, 100);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.tableWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(405)
        self.frame = QFrame(self.pg_usuario)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 10, 461, 80))
        self.frame.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 81 12pt \"Ubuntu\";\n"
"image:rgb(94, 92, 100);\n"
"background-color: rgb(94, 92, 100);\n"
"")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, -4, 111, 31))
        font5 = QFont()
        font5.setFamilies([u"Ubuntu"])
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 81 15pt \"Ubuntu\";\n"
"image:rgb(94, 92, 100);\n"
"background-color: rgb(94, 92, 100);")
        self.txt_email = QLineEdit(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(10, 30, 231, 25))
        self.txt_email.setFocusPolicy(Qt.ClickFocus)
        self.txt_email.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.txt_email.setAcceptDrops(True)
        self.txt_email.setAutoFillBackground(False)
        self.txt_email.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(61, 56, 70);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(154, 153, 150);\n"
"}")
        self.txt_email.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(260, 30, 181, 25))
        self.txt_senha.setFocusPolicy(Qt.ClickFocus)
        self.txt_senha.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"	background-color: rgb(61, 56, 70);\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(154, 153, 150);\n"
"}")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setDragEnabled(False)
        self.txt_senha.setReadOnly(False)
        self.stackedWidget.addWidget(self.pg_usuario)
        self.pg_corpo = QWidget()
        self.pg_corpo.setObjectName(u"pg_corpo")
        self.pg_corpo.setStyleSheet(u"image: url(:/pic_qt/centro.png);")
        self.barra_deprogresso = QProgressBar(self.pg_corpo)
        self.barra_deprogresso.setObjectName(u"barra_deprogresso")
        self.barra_deprogresso.setGeometry(QRect(0, 610, 871, 23))
        self.barra_deprogresso.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.barra_deprogresso.setValue(0)
        self.txt_corpo = QPlainTextEdit(self.pg_corpo)
        self.txt_corpo.setObjectName(u"txt_corpo")
        self.txt_corpo.setGeometry(QRect(10, 50, 411, 461))
        self.txt_corpo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"color: rgb(36, 31, 49);")
        self.txt_corpo.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.label_2 = QLabel(self.pg_corpo)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 191, 31))
        font6 = QFont()
        font6.setFamilies([u"Ubuntu"])
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"font: 81 20pt \"Ubuntu\";\n"
"image:none;\n"
"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_3 = QLabel(self.pg_corpo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(580, 10, 121, 31))
        self.label_3.setStyleSheet(u"font: 81 20pt \"Ubuntu\";\n"
"image:none;\n"
"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.txt_progresso = QPlainTextEdit(self.pg_corpo)
        self.txt_progresso.setObjectName(u"txt_progresso")
        self.txt_progresso.setEnabled(False)
        self.txt_progresso.setGeometry(QRect(440, 50, 421, 461))
        self.txt_progresso.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
"\n"
"color: rgb(36, 31, 49);")
        self.btn_anexo = QPushButton(self.pg_corpo)
        self.btn_anexo.setObjectName(u"btn_anexo")
        self.btn_anexo.setGeometry(QRect(160, 560, 101, 31))
        self.btn_anexo.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(94, 92, 100);\n"
"	image:rgb(94, 92, 100);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(97, 53, 131);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/pic_qt/adcemail.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_anexo.setIcon(icon8)
        self.btn_anexo.setIconSize(QSize(28, 28))
        self.lineEdit = QLineEdit(self.pg_corpo)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 520, 411, 25))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(165, 29, 45);")
        self.stackedWidget.addWidget(self.pg_corpo)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_centro)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_enviar, self.btn_menu)
        QWidget.setTabOrder(self.btn_menu, self.btn_config)
        QWidget.setTabOrder(self.btn_config, self.btn_corpo)
        QWidget.setTabOrder(self.btn_corpo, self.btn_adicionar)
        QWidget.setTabOrder(self.btn_adicionar, self.btn_excluir_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.btn_adicionar.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Envio de E-mail", None))
        self.btn_menu.setText("")
        self.btn_enviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.btn_corpo.setText(QCoreApplication.translate("MainWindow", u"Corpo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BruTha", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.stackedWidget.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.stackedWidget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.stackedWidget.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.btn_adicionar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btn_adicionar.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
#if QT_CONFIG(shortcut)
        self.btn_adicionar.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.txt_destino.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Destinat\u00e1rio", None))
        self.txt_funcao.setText("")
        self.txt_funcao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None))
        self.btn_excluir_2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Login g-mail", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu e-mail.", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Corpo do E-mail", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Progresso", None))
        self.txt_progresso.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Acompanhar envio.....", None))
        self.btn_anexo.setText(QCoreApplication.translate("MainWindow", u"Anexo", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Caminho do anexo", None))
    # retranslateUi

