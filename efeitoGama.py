import sys
from PIL import Image

#abrindo img
if __name__== "__main__":
    #print(f'Quantos argumentos:{len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        if i == 1:
                entradaPrincipal = arg
        saidaPrincipal = arg

#abrir os arquivos de entrada e saida 
img1 = Image.open(entradaPrincipal)

#carregar imag para matriz 
matrix = img1.load()


gamma = 3.0
for i in range(img1.size[0]):
    for j in range(img1.size[1]):
        r = int((matrix[i, j][0]/255)** gamma * 255)
        g = int((matrix[i, j][1]/255)** gamma * 255)
        b = int((matrix[i, j][2]/255)** gamma * 255)
        matrix[ i, j] = (r, g, b)

img1.save(saidaPrincipal)   
