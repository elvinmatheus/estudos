# -*- coding: utf-8 -*-
"""1183.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13cSD1jRKAAbE_KR8M_JPP2wvblWAvWbA
"""

def matriz(lins, cols, val_inic):
     m = [[val_inic] * cols for _ in range(lins)]
     return m

M = matriz(12,12,0.0)
O = str(input())

for i in range(12):
  for j in range(12):
    M[i][j] = float(input())

soma = 0.0
media = 0.0
for i in range(12):
  for j in range(12):
    if j > i:
      soma = soma + M[i][j]
      
if O == 'S':
  print('{:.1f}'.format(soma))
if O == 'M':
  media = soma / 66
  print('{:.1f}'.format(media))