# -*- coding: utf-8 -*-
"""1042.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HbOxxMAV6iMJy5dk9Iyn5vuoV6WhFVtm
"""

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a > b and a > c:
  maior = a
  if b > c:
    meio = b
    menor = c
  else:
    meio = c
    menor = b

if b > a and b > c:
  maior = b
  if a > c:
    meio = a
    menor = c
  else:
    meio = c
    menor = a

if c > a and c > b:
  maior = c
  if a > b:
    meio = a
    menor = b
  else:
    meio = b
    menor = a

print(menor)
print(meio)
print(maior)
print()
print(a)
print(b)
print(c)