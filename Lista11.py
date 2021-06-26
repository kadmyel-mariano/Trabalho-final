from PIL import Image
from PyQt5.QtWidgets import *
import sys

if __name__== "__main__":
    #print(f'Quantos argumentos:{len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        if i == 1:
                entradaPrincipal = arg
        saidaPrincipal = arg

img = Image.open(entradaPrincipal)

imgpng = img.convert('RGBA')

#verifica quais bandas a imagem tem
print(img.getbands())
print(img.getbands())

#Obtem uma lista com os pixels da imagem
pixels = list(imgpng.getdata())
print(pixels[0])
print(type(pixels))

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(40)
        self.dial.valueChanged.connect(self.sliderMoved)
        layout.addWidget(self.dial)

    def sliderMoved(self):
        print("Dial value = %i" % (self.dial.value()))
    

#salvar a imagem nova
#criar uma imagem nova
outputImg = Image.new('RGBA', img.size)
#pixels alterado
outputImg.putdata(pixels)
#salvar
outputImg.save('edit.png')
