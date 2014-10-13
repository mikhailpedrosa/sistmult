# -*- coding: utf-8 -*-
__author__ = 'Mikhail Pedrosa <mikhail.jose@hotmail.com> e Tiago AlvesTiago Alves <tiagoinformativa@gmail.com >'
__description__ = 'Operações com Imagens - Histograma, Operações Pontuais, Lógicas, Aritméticas, Translação, Rotação e Escala'
__version__ = '0.1'
__date__ = '15/09/2014'


from scipy import ndimage
from pylab import *
from PIL import Image
import PIL
import scipy
import matplotlib.pyplot as plt
import numpy as np


#Bibliotecas Usadas - matplotlib, numpy, pillow
#Python 2.7

def histogram(imagem1, imagem2):
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


def rotacao(imagem1):
    imagem1 = Image.open("foto1.jpg")
    # Rotação da Imagem 90 graus e 180 graus
    rot_90 = imagem1.transpose(Image.ROTATE_90)
    rot_90 = rot_90.save("rotacao_90.png")
    rot_180 = imagem1.transpose(Image.ROTATE_180)
    rot_180 = rot_180.save("rotacao_180.png")

    return rot_90, rot_180


def espelhamento(imagem1):
    imagem1 = Image.open("foto1.jpg")
    left_right = imagem1.transpose(Image.FLIP_LEFT_RIGHT)
    left_right = left_right.save("espelhamento_left_right.png")
    top = imagem1.transpose(Image.FLIP_TOP_BOTTOM)
    top = top.save("espelhamento_top.png")

    return left_right, top


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
                print #"You can't divide by zero, you're silly."

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


def escala(imagem1):
    #Largura da Base
    basewidth=300
    #Porcento da Altura
    wpercent = (basewidth/float(imagem1.size[0]))
    #Tamanho da Altura
    hsize = int((float(imagem1.size[1])*float(wpercent)))
    imagem_menor = imagem1.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
    lar=1500
    alt = 1000
    imagem_maior = imagem1.resize((lar,alt))

    return imagem_menor.save('escala_menor.png'), imagem_maior.save("escala_maior.png")

def translacao():
    imagem = Image.open("foto.png")
    #Tamanho Imagem - Largura e Altura
    lar = imagem.size[0]
    alt = imagem.size[1]
    x_loc = 100
    y_loc = 150
    imagem_matriz = np.asarray(imagem.convert('RGB'))
    for x in range(lar):
        for y in range(alt):
            if x >= x_loc and y >= y_loc:
                yo = x - x_loc
                xo = y - y_loc
                imagem.putpixel((x,y), (imagem_matriz[xo,yo][0],imagem_matriz[xo,yo][1],imagem_matriz[xo,yo][2]))
            else:
                imagem.putpixel((x,y), (255, 255, 255, 255))

    return imagem.save("translate.png")


def desfoque_alisamento(imagem):

    blurred_lena = ndimage.gaussian_filter(imagem, sigma=3)
    very_blurred = ndimage.gaussian_filter(imagem, sigma=5)
    local_mean = ndimage.uniform_filter(imagem, size=11)

    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.imshow(blurred_lena, cmap=plt.cm.gray)
    plt.axis('off')
    plt.subplot(132)
    plt.imshow(very_blurred, cmap=plt.cm.gray)
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(local_mean, cmap=plt.cm.gray)
    plt.axis('off')

    plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
                        left=0.01, right=0.99)
    plt.show()

def afinacao(imagem):

    blurred_imagem = ndimage.gaussian_filter(imagem, 3)
    filter_blurred_imagem = ndimage.gaussian_filter(blurred_imagem, 1)

    alpha = 30
    sharpened = blurred_imagem + alpha * (blurred_imagem - filter_blurred_imagem)

    plt.figure(figsize=(12, 4))

    plt.subplot(131)
    plt.imshow(imagem, cmap=plt.cm.gray)
    plt.axis('off')
    plt.subplot(132)
    plt.imshow(blurred_imagem, cmap=plt.cm.gray)
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(sharpened, cmap=plt.cm.gray)
    plt.axis('off')

    plt.show()

def suavizacao():

    imagem = scipy.misc.lena()
    imagem = imagem[230:290, 220:320]

    noisy = imagem + 0.4*imagem.std()*np.random.random(imagem.shape)
    gauss_denoised = ndimage.gaussian_filter(noisy, 2)
    med_denoised = ndimage.median_filter(noisy, 3)


    plt.figure(figsize=(12,2.8))
    plt.subplot(131)
    plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.title('Noisy', fontsize=20)
    plt.subplot(132)
    plt.imshow(gauss_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.title('Gaussian filter', fontsize=20)
    plt.subplot(133)
    plt.imshow(med_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.title('Median filter', fontsize=20)
    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,
                        right=1)
    plt.show()


if __name__ == '__main__':
    # Leitura das Imagens e Conversão para RGB
    imagem1 = Image.open("foto1.jpg").convert('RGB')
    imagem2 = Image.open("foto2.jpg").convert('RGB')

    #Histograma
    #histogram(imagem1, imagem2)

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
    #desfoque_alisamento(imagem1)
    afinacao(imagem1)
    suavizacao()

    #Transformações Geométricas
    #translacao()

    #Rotação
    #rotacao(imagem1)

    #Escala
    #escala(imagem1)

    #Espelhamento ou Reflexão
    #espelhamento(imagem1)

