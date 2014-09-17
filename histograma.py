# -*- coding: utf-8 -*-
__author__ = 'Mikhail Pedrosa <mikhail.jose@hotmail.com>'
__description__ = 'Verifica arquivos RAWs copiados e cria os produtos PPI e CAPPI .dat.'
__version__ = '0.1'
__date__ = '15/09/2014'

import matplotlib.pyplot as plot
import numpy as np
from PIL import Image
from pylab import *

def gerarHist(matriz):
    plot.hist(matriz.flatten(), color='green')
    plot.title = ('Histograma')
    plot.show()

if __name__ == '__main__':

    imagem = Image.open("logotipoceara.jpg")
    matriz = np.asarray(imagem.convert('L'))

    #r, g, b = imagem.split()
    #im = Image.merge("RGB", (b, g, r))

    gerarHist(matriz)
