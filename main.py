#Criando interface grafica com Python
import sys
import subprocess
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setup_main_window()
        self.initUI()
      

    def setup_main_window(self):
     self.x = 640 
     self.y = 480 
     self.setMinimumSize(QSize(self.x, self.y))
     self.setWindowTitle("Editor The Pro")
     self.wid = QWidget(self)
     self.setCentralWidget(self.wid)
     self.layout = QGridLayout()
     self.wid.setLayout(self.layout)

    def initUI(self):

        # Criando barra de menu

        self.barraDeMenu = self.menuBar()   

        # Criando os menus

        self.menuArquivo = self.barraDeMenu.addMenu("&Arquivo")
        self.tranformacao = self.barraDeMenu.addMenu("&Tranformações")
        self.menusobre = self.barraDeMenu.addMenu("&Sobre")        

        # Criando as actions menuArquivo

        self.opcaoabrir = self.menuArquivo.addAction("Abrir")
        self.opcaosalvar = self.menuArquivo.addAction("Salvar como")
        self.opcaoFechar = self.menuArquivo.addAction("Fechar")
        self.opcaoabrir.triggered.connect(self.open_file)
        self.opcaoabrir.setShortcut("Ctrl+A")
        self.opcaoFechar.triggered.connect(self.close)
        self.opcaoFechar.setShortcut("Alt+F4")
        
        # EFEITO TRANSFORMAÇÃO

        self.opcaoefeito = self.tranformacao.addMenu("Efeitos")

        self.efeito_Blur  = self.opcaoefeito.addAction("Efeito blur")
        self.efeito_Blur.triggered.connect(self.efeitoBlur)
        self.tranformacao.addSeparator()

        self.efeito_Contour  = self.opcaoefeito.addAction("Efeito Contour")
        self.efeito_Contour.triggered.connect(self.efeitoContour)
        self.tranformacao.addSeparator()

        self.efeito_Emboss  = self.opcaoefeito.addAction("Efeito Emboss")
        self.efeito_Emboss.triggered.connect(self.efeitoEmboss)
        self.tranformacao.addSeparator()

        self.efeito_Detail  = self.opcaoefeito.addAction("Efeito Detail")
        self.efeito_Detail.triggered.connect(self.efeitoDetail)
        self.tranformacao.addSeparator() 

        self.efeito_EDGE_ENHANCE  = self.opcaoefeito.addAction("Efeito EDGE_ENCHACE")
        self.efeito_EDGE_ENHANCE.triggered.connect(self.efeitoEDGE_ENHANCE)
        self.tranformacao.addSeparator()   

        self.efeito_EDGE_ENHANCE_MORE  = self.opcaoefeito.addAction("Efeito EDGE_ENCHACE_MORE")
        self.efeito_EDGE_ENHANCE_MORE.triggered.connect(self.efeitoEDGE_ENHANCE_MORE)
        self.tranformacao.addSeparator() 

        self.efeito_FIND_EDGES  = self.opcaoefeito.addAction("Efeito FIND_EDGES")
        self.efeito_FIND_EDGES.triggered.connect(self.efeitoFIND_EDGES)
        self.tranformacao.addSeparator() 

        self.efeito_SHARPEN = self.opcaoefeito.addAction("Efeito SHARPEN")
        self.efeito_SHARPEN.triggered.connect(self.efeitoSHARPEN)
        self.tranformacao.addSeparator()

        self.efeito_SMOOTH_MORE  = self.opcaoefeito.addAction("Efeito SMOOTH_MORE")
        self.efeito_SMOOTH_MORE.triggered.connect(self.efeitoSMOOTH_MORE)
        self.tranformacao.addSeparator() 

        self.efeito_SMOOTH  = self.opcaoefeito.addAction("Efeito SMOOTH")
        self.efeito_SMOOTH.triggered.connect(self.efeitoSMOOTH)
        self.tranformacao.addSeparator() 

        # EFEITO GAMMA E NEGATIVO

        self.efeito_Negativo  = self.tranformacao.addAction("Efeito NEGATIVO")
        self.efeito_Negativo.triggered.connect(self.efeitoNegativo)
        self.tranformacao.addSeparator()          
        self.efeito_Gama  = self.tranformacao.addAction("Efeito GAMMA")
        self.efeito_Gama.triggered.connect(self.efeitoGama)
        self.tranformacao.addSeparator()

         # EFEITO GAMMA E NEGATIVO   

        self.opcaoBordas = self.tranformacao.addMenu("Bordas")
        
        self.efeito_bordas  = self.opcaoBordas.addAction("Borda 1")
        self.efeito_bordas.triggered.connect(self.efeitoBordas)
        self.tranformacao.addSeparator() 
        self.efeito_bordas2  = self.opcaoBordas.addAction("Borda 2")
        self.efeito_bordas2.triggered.connect(self.efeitoBordas2)
        self.tranformacao.addSeparator()  
        self.efeito_bordas3  = self.opcaoBordas.addAction("Borda 3")
        self.efeito_bordas3.triggered.connect(self.efeitoBordas3)
        self.tranformacao.addSeparator() 

        # EFEITO GAMMA E NEGATIVO   

        self.opcaoEscala = self.tranformacao.addMenu("Escala")

        self.efeito_escalaCinza  = self.opcaoEscala.addAction("Escala Cinza")
        self.efeito_escalaCinza.triggered.connect(self.escalaCinza)
        self.tranformacao.addSeparator()          
        self.efeito_escalaPretoeBranco  = self.opcaoEscala.addAction("Escala Preto e Branco")
        self.efeito_escalaPretoeBranco.triggered.connect(self.escalaPretoeBranco)
        self.tranformacao.addSeparator()

        # EFEITO GAMMA E NEGATIVO   

        self.opcaoCamada = self.tranformacao.addMenu("Camada")

        self.efeito_camadaR = self.opcaoCamada.addAction("Camada R")
        self.efeito_camadaR.triggered.connect(self.camadaR)
        self.tranformacao.addSeparator()
        self.efeito_camadaG = self.opcaoCamada.addAction("Camada G")
        self.efeito_camadaG.triggered.connect(self.camadaG)
        self.tranformacao.addSeparator()
        self.efeito_camadaB = self.opcaoCamada.addAction("Camada B")
        self.efeito_camadaB.triggered.connect(self.camadaB)
        self.tranformacao.addSeparator()
        
        self.efeito_transparencia = self.tranformacao.addAction("Transformação")
        self.efeito_transparencia.triggered.connect(self.transparencia)
        self.tranformacao.addSeparator()
        #barra do sobre
        self.opcaosobre =self.menusobre.addAction("Sobre o aplicativo")
        self.opcaosobre.triggered.connect(self.exibe_mensagem)

        self.opcaosobre = self.menusobre.addAction("Sobre a imagem")
        self.opcaosobre.triggered.connect(self.exibe_dados_imagem)
        self.opcaoapagar = self.menusobre.addAction("Apagar")
        self.opcaoapagar.triggered.connect(self.apagar_mensagem)

        #barra de status
        self.barradestatus = self.statusBar()
        self.barradestatus.showMessage("Oi,Kadmyel e Kennes sou a Barra de Status",)

       

    #TEXTO 
        self.texto = QLabel("Processamento digital de imagens - IFTM ", self)
        self.texto.adjustSize()
        self.largura = self.texto.frameGeometry().width()
        self.altura = self.texto.frameGeometry().height()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)

        # janela 
        self.imagem1 = QLabel(self)
        self.endereco1 = 'iftm.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1) 
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        self.imagem2 = QLabel(self)
        self.endereco2 = 'iftm.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        #Organização
        self.layout.addWidget(self.texto, 0, 0, 1, 2)
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 0)
     
    #metodo para opcao sobre
    def apagar_mensagem(self):
        self.barradestatus.clearMessage()
    
    def exibe_dados_imagem(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Sobre o Imagem")
        self.msg.setText("iftm\n.jpg\n imagem editada para a construção do aplicativo \n largura: 225\n altura:225")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()
        self.reply = self.msg.clickedButton()
        self.barradestatus.showMessage("Foi clicado o botão: " + self.reply.text())


    def exibe_mensagem(self):
        #self.barradestatus.showMessage("Oi sou o Aplicativo ...")
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle("Sobre o Aplicativo")
        self.msg.setText("Kadmyel Mariano Silva Nunes\nKennes Eduardo Marques Silva")
        self.msg.setInformativeText("Ituiutaba-MG,26 de Junho de 2020")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.exec_()
        self.reply = self.msg.clickedButton()
        self.barradestatus.showMessage("Foi clicado o botão: " + self.reply.text())

     #metodos para açoes dos botoes

    def open_file(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption = "Abrir Imagem", directory= QtCore.QDir.currentPath(), 
        filter= 'all files(*.*);;Images (*.ppm; *pgm; *.pbm; *.jpg; *.jpeg', initialFilter = 'Images(*.ppm; *pgm; *.pbm; *.jpg; *.jpeg')

        print(fileName)
        self.endereco1 = fileName
        self.pixmap1 = QtGui.QPixmap(self.endereco1)
        self.pixmap1 = self.pixmap1.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1) 
    
    def efeitoBlur(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoBlur.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        
    def efeitoContour(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoContour.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        
    def efeitoEmboss(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoEmboss.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def efeitoDetail(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitodetail.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)  

    def efeitoEDGE_ENHANCE_MORE(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoEDGE_ENHANCE_MORE.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)   

    def efeitoFIND_EDGES(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoFIND_EDGES.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
               
    def efeitoEDGE_ENHANCE(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoEDGE_ENHANCE.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def efeitoSHARPEN(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoSHARPEN.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)

    def efeitoSMOOTH_MORE(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoSMOOTH_MORE.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)       

    def efeitoSMOOTH(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoSMOOTH.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)  

    def efeitoNegativo(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoNegativo.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2) 

    def efeitoGama(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoGama.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)  

    def efeitoBordas(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoBordas.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)    

    def efeitoBordas2(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoBordas2.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)   

    def efeitoBordas3(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\efeitoBordas3.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)   

    def escalaCinza(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\escalaCinza.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)    

    def escalaPretoeBranco(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\escalaPretoeBranco.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)  

    def camadaR(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\camadaR.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)   

    def camadaG(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\camadaG.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)   

    def camadaB(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '.\camadaB.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida
        #print(self.program) 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)   

    def transparencia(self):
        self.entrada = self.endereco1
        self.saida = 'arquivo_novo.jpg'
        self.script = '\Lista11.py'
        self.program = 'python '+ self.script + ' \"' + self.entrada + '\" ' + self.saida 
        subprocess.run(self.program, shell=True)
        self.endereco2 = self.saida
        self.pixmap2 = QtGui.QPixmap(self.endereco2)
        self.pixmap2 = self.pixmap2.scaled(250, 250, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)   
                                                                               
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_()) 

window()