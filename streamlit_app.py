#import principal
import streamlit as st
#imports relacionados
from PIL import Image
import pytesseract
#metodos internos
import functions.functions as fc
import pandas as pd
import numpy as np

class OCR:

    def __init__(self):
        self.texto = ""
        self.analizar_texto = False

    def inicial(self):
        #Contenido inicial de la página
        st.title("Sistema integrado de inventarios")
        option = st.selectbox('Proveedor', ('Proveedor 1', 'Proveedor 2', 'Proveedor 3', 'Otro'))
        st.write('Proveedor:', option)
        num_prod = st.number_input('Número de productos', min_value=1, max_value=1000000, value=1, step=1)
        st.write("Escaneo de etiqueta")
        imagem = st.file_uploader("escanear etiqueta", type=["png","jpg"])
        #Se selecciona alguna imagen...
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=350)
            st.info("Texto extraído")
            self.texto = self.extrair_texto(img)
            st.write(f"{self.texto}")
            if "SKU" in self.texto:
              sku = self.texto.split("SKU")[1].split("\n")[0]
              sku = [int(x) for x in sku.split() if x.isdigit()][0]
              st.write(f"SKU del producto registrado: {sku}")

            if "RFC" in self.texto:
              rfc = self.texto.split("RFC")[1].split("\n")[0]
              rfc = rfc.replace('#', '').replace(' ','').replace(':','')
              st.write(f"RFC del vendedor registrado: {rfc}")
            
            if st.button('Enviar'):
                st.write('Enviado')
            else:
                st.write('Revisa la entrada antes de enviar')
            
            #Opcao de analisar texto
            #self.analisar_texto = st.sidebar.checkbox("Analizar texto")
            #if self.analisar_texto==True:
            #    self.mostrar_analise()
        '''
        picture = st.camera_input("Take a picture")
        if picture:
            st.image(picture, width=350)
            st.info("Texto extraído")
            self.texto = self.extrair_texto(img)
            st.write(f"{self.texto}")
            if "SKU" in self.texto:
              sku = self.texto.split("SKU")[1].split("\n")[0]
              sku = [int(x) for x in sku.split() if x.isdigit()][0]
              st.write(f"SKU del producto registrado: {sku}")

            if "RFC" in self.texto:
              rfc = self.texto.split("RFC")[1].split("\n")[0]
              rfc = rfc.replace('#', '').replace(' ','').replace(':','')
              st.write(f"RFC del vendedor registrado: {rfc}")
            
            if st.button('Enviar'):
                st.write('Enviado')
            else:
                st.write('Revisa la entrada antes de enviar')
           '''     
    def extrair_texto(self, img):
        #O comando que extrai o texto da imagem
        texto = pytesseract.image_to_string(img)
        return texto
    

ocr = OCR()
ocr.inicial()
