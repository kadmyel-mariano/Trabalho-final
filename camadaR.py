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
matrixR = img.load()

#realizar as operações pixel a pixel 
for i in range(img.size[0]):
    for j in range(img.size[1]):
        matrixR[ i, j] = (255, 0, 0)

img.save(saidaPrincipal)    

