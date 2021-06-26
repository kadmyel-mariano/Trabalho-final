# -*- coding: utf:8 -*-
import sys

from PIL import Image, ImageFilter

#convertendo uma imagem colorida para esqcala de cinza

if __name__== "__main__":
    #print(f'Quantos argumentos:{len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        if i == 1:
                entradaPrincipal = arg
        saidaPrincipal = arg

#abrir os arquivos de entrada e saida 
img1 = Image.open(entradaPrincipal)

img2 = img1.filter(ImageFilter.SHARPEN)

img2.save(saidaPrincipal)
