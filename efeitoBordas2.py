import sys
from PIL import Image, ImageFilter

#abrindo img
if __name__== "__main__":
    #print(f'Quantos argumentos:{len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        if i == 1:
                entradaPrincipal = arg
        saidaPrincipal = arg

#abrir os arquivos de entrada e saida 
img1 = Image.open(entradaPrincipal)

#ciando kernel 

kernel1= ImageFilter.Kernel((3,3),(0,1,0,1,-4,1,0,1,0,), 1, 0)

#aplicando kernel
img2 = img1.filter(kernel1)

img2.save(saidaPrincipal)  