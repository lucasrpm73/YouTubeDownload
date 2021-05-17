# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:54:18 2021

@author: Lucas Santos
"""

import webbrowser 

url = input("Digite o link do Vídeo:")

url = url[:12]+'ss'+url[12:]

webbrowser.open(url)