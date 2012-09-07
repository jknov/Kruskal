#!/usr/bin/python

from GraphForApp import *


def mezcla(E,i,mid,f):
   it1 = i
   it2 = mid+1
   T = []
   while it1 <= mid and it2 <= f:
      if E[it1].getPeso() < E[it2].getPeso():
         T.append(E[it1])
         it1 += 1
      else:
         T.append(E[it2])
         it2 += 1
   while it1 <= mid:
      T.append(E[it1])
      it1 += 1
   while it2 <= f:
      T.append(E[it2])
      it2 += 1
   j = i
   for x in T:
      E[j] = x
      j += 1

def ordenaAristasPorPeso(E,i,f):
   if i < f:
      mid = ((f-i+1)/2) + i - 1
      ordenaAristasPorPeso(E,i,mid)
      ordenaAristasPorPeso(E,mid+1,f)
      mezcla(E,i,mid,f)

def creaMatrizAux(V):
   M = [[0 for v in V] for v in V]
   return M


def kruskal(E,V):
   ordenaAristasPorPeso(E,0,len(E)-1)
   M = creaMatrizAux(V)
   T = []
   for e in E:
      [v,u] = e.getEndpoints()
      i = v.getIndice()
      j = u.getIndice()
      print e.getPeso()
      if M[i][j] == 0:
         T.append(e)
         M[i][j] = 1
         M[j][i] = 1
         for r in range(0,len(V)):
            if M[i][r] == 1:
               M[j][r] = 1
               M[r][j] = 1
            if M[j][r] == 1:
               M[i][r] = 1
               M[r][i] = 1
   for R in M:
      cont = 0
      for x in R:
         cont += x
      if cont < len(V)-1:
         print "no es conexa"
         return T
   return T
   

   
   
   
   
   
   