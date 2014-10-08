# -*- coding: utf-8 -*-
__author__ = 'Mikhail Pedrosa <mikhail.jose@hotmail.com> e Tiago Alves'
__description__ = 'Operações com Imagens - Histograma, Operações Pontuais, Lógicas, Aritméticas, Translação, Rotação e Escala'
__version__ = '0.1'
__date__ = '15/09/2014'

import matplotlib.pyplot as plt
import numpy as np
import PIL
from PIL import Image
from pylab import *


def gerarHist(imagem1, imagem2):
    matriz1 = np.asarray(imagem1.convert('L'))
    matriz2 = np.asarray(imagem2.convert('L'))

    # Visualização do Histograma (FotoCinza)
    plt.hist(matriz1.flatten(), color='green')
    plt.title('Histograma')
    plt.xlabel('Pixel')
    plt.ylabel('Ocorrencias')
    plt.show()

    # Visualização do Histograma (FotoCinza2)
    plt.hist(matriz2.flatten(), color='red')
    plt.title('Histograma')
    plt.xlabel('Pixel')
    plt.ylabel('Ocorrencias')
    plt.show()


def rotacao(imagem1, imagem2):
    # Rotação da Imagem 90 graus e 180 graus
    imagem1.transpose(Image.ROTATE_90).show(title='Imagem 90')
    imagem1.transpose(Image.ROTATE_180).show(title='Imagem 180')

    imagem2.transpose(Image.ROTATE_90).show(title='Imagem 90')
    imagem2.transpose(Image.ROTATE_180).show(title='Imagem 180')


def espelhamento(imagem1, imagem2):
    imagem1.transpose(Image.FLIP_LEFT_RIGHT).show()
    imagem1.transpose(Image.FLIP_TOP_BOTTOM).show()

    imagem2.transpose(Image.FLIP_LEFT_RIGHT).show()
    imagem2.transpose(Image.FLIP_TOP_BOTTOM).show()


def soma(imagem1, imagem2):

    #Tamanho (Altura e Largura)
    im1_W = imagem1.size[0]
    im1_H = imagem2.size[1]

    for y in xrange(0, im1_H):
        for x in xrange(0, im1_W):
            xy = (x, y)
            #Função que pega os Pixel das Imagens 1 e 2
            red_im1, green_im1, blue_im1 = imagem1.getpixel(xy)
            red_im2, green_im2, blue_im2 = imagem2.getpixel(xy)

            #Operação Soma
            red_im1 += red_im2
            green_im1 += green_im2
            blue_im1 += blue_im2

            #Junção dos Pixels das Imagens
            imagem1.putpixel((x, y), (red_im1, green_im1, blue_im1))

    return imagem1.save('soma.png')

def subt(imagem1, imagem2):

    #Tamanho (Altura e Largura)
    im1_W = imagem1.size[0]
    im1_H = imagem2.size[1]

    for y in xrange(0, im1_H):
        for x in xrange(0, im1_W):
            xy = (x, y)
            #Função que pega os Pixel das Imagens 1 e 2
            red_im1, green_im1, blue_im1 = imagem1.getpixel(xy)
            red_im2, green_im2, blue_im2 = imagem2.getpixel(xy)

            #Operação Subtração
            red_im1 -= red_im2
            green_im1 -= green_im2
            blue_im1 -= blue_im2

            #Junção dos Pixels das Imagens
            imagem1.putpixel((x, y), (red_im1, green_im1, blue_im1))

    return imagem1.save('sub.png')

def mult(imagem1, imagem2):

    #Tamanho (Altura e Largura)
    im1_W = imagem1.size[0]
    im1_H = imagem2.size[1]

    for y in xrange(0, im1_H):
        for x in xrange(0, im1_W):
            xy = (x, y)
            #Função que pega os Pixel das Imagens 1 e 2
            red_im1, green_im1, blue_im1 = imagem1.getpixel(xy)
            red_im2, green_im2, blue_im2 = imagem2.getpixel(xy)

            #Operação Multiplicção
            red_im1 *= red_im2
            green_im1 *= green_im2
            blue_im1 *= blue_im2

            #Junção dos Pixels das Imagens
            imagem1.putpixel((x, y), (red_im1, green_im1, blue_im1))

    return imagem1.save('mult.png')

def div(imagem1, imagem2):

    #Tamanho (Altura e Largura)
    im1_W = imagem1.size[0]
    im1_H = imagem2.size[1]

    for y in xrange(0, im1_H):
        for x in xrange(0, im1_W):
            xy = (x, y)
            #Função que pega os Pixel das Imagens 1 e 2
            red_im1, green_im1, blue_im1 = imagem1.getpixel(xy)
            red_im2, green_im2, blue_im2 = imagem2.getpixel(xy)

            #Operação Divisão
            try:
                red_im1 /= red_im2
                green_im1 /= green_im2
                blue_im1 /= blue_im2
            except ZeroDivisionError:
                print "You can't divide by zero, you're silly."

            #Junção dos Pixels das Imagens
            imagem1.putpixel((x, y), (red_im1, green_im1, blue_im1))

    return imagem1.save('div.png')


def E(imagem1, imagem2):

    #Tamanho (Altura e Largura)
    im1_W = imagem1.size[0]
    im1_H = imagem2.size[1]

    for y in xrange(0, im1_H):
        for x in xrange(0, im1_W):
            xy = (x, y)
            #Função que pega os Pixel das Imagens 1 e 2
            red_im1, green_im1, blue_im1 = imagem1.getpixel(xy)
            red_im2, green_im2, blue_im2 = imagem2.getpixel(xy)

            #Operação AND

            red_im1 and red_im2
            green_im1 and green_im2
            blue_im1 and blue_im2


            #Junção dos Pixels das Imagens
            imagem1.putpixel((x, y), (red_im1, green_im1, blue_im1))

    return imagem1.save('and.png')

def OU(imagem1, imagem2):

    #Tamanho (Altura e Largura)
    im1_W = imagem1.size[0]
    im1_H = imagem2.size[1]

    for y in xrange(0, im1_H):
        for x in xrange(0, im1_W):
            xy = (x, y)
            #Função que pega os Pixel das Imagens 1 e 2
            red_im1, green_im1, blue_im1 = imagem1.getpixel(xy)
            red_im2, green_im2, blue_im2 = imagem2.getpixel(xy)

            #Operação OU

            red_im1 or red_im2
            green_im1 or green_im2
            blue_im1 or blue_im2


            #Junção dos Pixels das Imagens
            imagem1.putpixel((x, y), (red_im1, green_im1, blue_im1))

    return imagem1.save('or.png')

def XOR(imagem1, imagem2):

    #Tamanho (Altura e Largura)
    im1_W = imagem1.size[0]
    im1_H = imagem2.size[1]

    for y in xrange(0, im1_H):
        for x in xrange(0, im1_W):
            xy = (x, y)
            #Função que pega os Pixel das Imagens 1 e 2
            red_im1, green_im1, blue_im1 = imagem1.getpixel(xy)
            red_im2, green_im2, blue_im2 = imagem2.getpixel(xy)

            #Operação OU

            red_im1 ^ red_im2
            green_im1 ^ green_im2
            blue_im1 ^ blue_im2


            #Junção dos Pixels das Imagens
            imagem1.putpixel((x, y), (red_im1, green_im1, blue_im1))

    return imagem1.save('xor.png')

def translacao (imagem1):
    destino = Image.open("foto.png")
    #Tamanho Imagem - Largura e Altura
    lar = destino.size[0]
    alt = destino.size[1]
    x_loc = 200
    y_loc = 200
    imagem_original = np.asarray(destino.convert('RGB'))
    for x in range(lar):
        for y in range(alt):
            if x >= x_loc and y >= y_loc:
                yo = x - x_loc
                xo = y - y_loc
                destino.putpixel((x,y), (imagem_original[xo,yo][0],imagem_original[xo,yo][1],imagem_original[xo,yo][2]))
            else:
                destino.putpixel((x,y), (255, 255, 255, 255))
    
    return destino.save("translate.png")


if __name__ == '__main__':
    # Leitura das Imagens e Conversão para RGB
    imagem1 = Image.open("foto1.jpg").convert('RGB')
    imagem2 = Image.open("foto2.jpg").convert('RGB')

    #Histograma
    #gerarHist(imagem1, imagem2)

    #Operações Pontuais
    #Operações Aritméticas (Soma, Subtração, Multiplicação, Divisão)
    #soma(imagem1, imagem2)
    #subt(imagem1, imagem2)
    #mult(imagem1, imagem2)
    #div(imagem1, imagem2)

    #Operações Lógicas (And, Ou, Xor)
    #E(imagem1, imagem2)
    #OU(imagem1, imagem2)
    #XOR(imagem1, imagem2)

    #Operações Locais


    #Transformações Geométricas
    #Translação


    #Rotação
    #rotacao(imagem1, imagem2)

    #Escala
    basewidth=300
    wpercent = (basewidth/float(imagem1.size[0]))
    hsize = int((float(imagem1.size[1])*float(wpercent)))
    imagem1 = imagem1.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    imagem1.save('escala_menor.jpg')
    #imagem1 = imagem1.resize()
    #imagem1.save('escala_maior.jpg')

    #Espelhamento ou Reflexão
    #espelhamento(imagem1, imagem2)

    #r, g, b = imagem.split()
    #im = Image.merge("RGB", (b, g, r))
