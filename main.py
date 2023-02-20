############################################################################
# Lê matriz RGB retângular em uma região específica da imagem
#############################################################################
import cv2 as cv
import numpy as np
import math
#*****************************************************************************
sR = 0
sG = 0
sB = 0
n = 1
#*****************************************************************************
img = cv.imread("/endereço/imagem/imagem.extençao")
img = np.copy(img)
# ****************************************************************************
def Retangulo(img):
    img = cv.rectangle(img,(220,100),(250,150),(200,0,0),3) # cria retângulo
    # iniciando nas coord/das ("X","Y"), e final/ndo nas coord/das ("x","y")
Retangulo(img)
# ****************************************************************************
for l in range (105,145):#105,145
    for c in range (225,245):#225,245 
        b,g,r = img[l,c] # Coordenadas "Y", "X"
        #*********************************************************************
        sR = sR+r 
        mR =sR/n # Média vermelho R
        MR = math.trunc(mR)
        #*********************************************************************
        sG = sG+g
        mG = sG/n # Média verde G
        MG = math.trunc(mG)
        #*********************************************************************
        sB = sB+b
        mB = sB/n # Média azul B
        MB = math.trunc(mB)
        #*********************************************************************
        n =n+1
        #*********************************************************************
        img[l,c]=[0,255,0]
        #*********************************************************************
        print( "L =",l, "C =",c, "| mR =",MR," mG ="
              ,MG," mB",MB)        
#*****************************************************************************
img=cv.putText(img,("  R   G   B"),(10,20),
               cv.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
img = cv.putText(img,str(MR),(10,40),
                 cv.FONT_HERSHEY_SIMPLEX,0.5,(50,50,50),1)
img = cv.putText(img,str(MG),(50,40),
                cv.FONT_HERSHEY_SIMPLEX,0.5,(50,50,50),1)
img = cv.putText(img,str(MB),(90,40),
                 cv.FONT_HERSHEY_SIMPLEX,0.5,(50,50,50),1)
#*****************************************************************************
cv.imshow("Caso Clinico", img)
# ****************************************************************************
#print("Dimensao/Canais",img.shape) # Imprime o número de pixels das
# dimensões "Y" e "X" da imagem, e também a quantidade de canais de cores 
# ****************************************************************************
cv.waitKey(0)
cv.destroyAllWindows()
###############################################################################