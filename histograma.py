# -*- coding: utf-8 -*-
__author__ = 'Mikhail Pedrosa <mikhail.jose@hotmail.com>'
__description__ = 'Cria Histograma a partir de uma Foto .jpg'
__version__ = '0.1'
__date__ = '15/09/2014'

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from pylab import *

def gerarHist(matriz):
    plt.hist(matriz.flatten(), color='green')
    plt.title('Histograma')
    plt.xlabel('Pixel')
    plt.ylabel('Ocorrencias')
    plt.show()

if __name__ == '__main__':

    imagem = Image.open("fotocinza2.jpg")
    matriz = np.asarray(imagem.convert('L'))

    #r, g, b = imagem.split()
    #im = Image.merge("RGB", (b, g, r))

    gerarHist(matriz)
