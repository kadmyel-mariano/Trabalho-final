import sys
from PIL import Image


if __name__== "__main__":
    #print(f'Quantos argumentos:{len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        if i == 1:
                entradaPrincipal = arg
        saidaPrincipal = arg

#abrir os arquivos de entrada e saida 
img1 = Image.open(entradaPrincipal)


matrix = img1.load()

#realizar as operações pixel a pixel 
for i in range(img1.size[0]):
    for j in range(img1.size[1]):
        r = 255 - matrix[i, j][0]
        g = 255 - matrix[i, j][1]
        b = 255 - matrix[i, j][2]
        matrix[ i, j] = (r, g, b)

#criando nova img editada.
img1.save(saidaPrincipal)        