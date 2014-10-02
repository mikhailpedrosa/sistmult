# -*- coding: utf-8 -*-
__author__ = 'Mikhail Pedrosa <mikhail.jose@hotmail.com> e Tiago Alves'
__description__ = 'Operações com Imagens - Histograma, Operações Pontuais, Lógicas, Aritméticas, Translação, Rotação e Escala'
__version__ = '0.1'
__date__ = '15/09/2014'

import matplotlib.pyplot as plt
import cv
import numpy as np
from PIL import Image
from pylab import *



def gerarHist(imagem1, imagem2):

    matriz1 = np.asarray(imagem1.convert('L'))
    matriz2 = np.asarray(imagem2.convert('L'))

    #Visualização do Histograma (FotoCinza)
    plt.hist(matriz1.flatten(), color='green')
    plt.title('Histograma')
    plt.xlabel('Pixel')
    plt.ylabel('Ocorrencias')
    plt.show()

    #Visualização do Histograma (FotoCinza2)
    plt.hist(matriz2.flatten(), color='red')
    plt.title('Histograma')
    plt.xlabel('Pixel')
    plt.ylabel('Ocorrencias')
    plt.show()


def rotacao(imagem1, imagem2):

    #Rotação da Imagem 90 graus e 180 graus
    imagem1.transpose(Image.ROTATE_90).show(title='Imagem 90')
    imagem1.transpose(Image.ROTATE_180).show(title='Imagem 180')

    imagem2.transpose(Image.ROTATE_90).show(title='Imagem 90')
    imagem2.transpose(Image.ROTATE_180).show(title='Imagem 180')


def espelhamento(imagem1, imagem2):

    imagem1.transpose(Image.FLIP_LEFT_RIGHT).show()
    imagem1.transpose(Image.FLIP_TOP_BOTTOM).show()

    imagem2.transpose(Image.FLIP_LEFT_RIGHT).show()
    imagem2.transpose(Image.FLIP_TOP_BOTTOM).show()

if __name__ == '__main__':

    #Leitura das Imagens
    imagem1 = Image.open("fotocinza.jpg")
    imagem2 = Image.open("fotocinza2.jpg")

    #Histograma
    #gerarHist(imagem1, imagem2)

    #Operações Pontuais
    #Operações Aritméticas (Soma, Subtração, Multiplicação, Divisão)
    rgb = imagem1.convert('RGB')

    #Operações Lógicas (And, Ou, Xor)

    #Operações Locais


    #Transformações Geométricas
    #Translação
    # img = imread('fotocinza.jpg',0)
    # rows, cols = shape(img)
    # #rows,cols = img.shape
    #
    # M = np.float32([[1,0,100],[0,1,50]])
    # dst = cv.warpAffine(img,M,(cols,rows))
    #
    # cv.imshow('img',dst)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    #Rotação
    #rotacao(imagem1, imagem2)

    #Escala


    #Espelhamento ou Reflexão
    espelhamento(imagem1, imagem2)

    #r, g, b = imagem.split()
    #im = Image.merge("RGB", (b, g, r))
