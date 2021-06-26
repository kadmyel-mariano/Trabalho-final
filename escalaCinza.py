import sys
from PIL import Image


if __name__== "__main__":
    #print(f'Quantos argumentos:{len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        if i == 1:
                entradaPrincipal = arg
        saidaPrincipal = arg

#abrir os arquivos de entrada e saida 
img = Image.open(entradaPrincipal)
#carregar imag para matriz 
matrix = img.load()

#realizar as operações pixel a pixel 
for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = matrix[i, j][0]
        g = matrix[i, j][1]
        b = matrix[i, j][2]
        pixel = int((r + g + b) / 3)#colocando ela em preto
        matrix[i,j] = (pixel, pixel, pixel)

#criando nova img editada.
img.save(saidaPrincipal)      