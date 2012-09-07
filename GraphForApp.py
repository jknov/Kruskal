#!/usr/bin/python

class Vertice:
   def __init__(self, ind, x0, y0,handler):
      self.indice = ind
      self.x = x0
      self.y = y0
      self.img = handler
   
   def getCoords(self):
      return [self.x,self.y]
   
   def getIndice(self):
      return self.indice
   
   def getImgHandler(self):
      return self.img
   

class Arista:
   def __init__(self, ind, v1, v2, p,handler):
      self.indice = ind
      self.v = v1
      self.u = v2
      self.peso = p
      self.img = handler
   
   def getIndice(self):
      return self.indice
   
   def getPeso(self):
      return self.peso
   
   def getEndpoints(self):
      return [self.v,self.u]
   
   
   def getImgHandler(self):
      return self.img
   
