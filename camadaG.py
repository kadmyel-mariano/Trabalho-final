import sys
from PIL import Image

if __name__== "__main__":
    #print(f'Quantos argumentos:{len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        if i == 1:
                entradaPrincipal = arg
        saidaPrincipal = arg

img = Image.open(entradaPrincipal)

#carregar imag para matriz 
matrixG = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        matrixG[ i, j] = (0, 255, 0)

img.save(saidaPrincipal)    

