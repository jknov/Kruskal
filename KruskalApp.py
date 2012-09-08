#!/usr/bin/python

from Tkinter import *
import math
import tkSimpleDialog
from Kruskal import kruskal
from GraphForApp import *
   

class MyDialog(tkSimpleDialog.Dialog):

    def body(self, master):

        Label(master, text="Peso:").grid(row=0)

        self.e1 = Entry(master)
        self.title("Dame el peso")

        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        self.result = int(self.e1.get())
   

class App:

   def __init__(self, master):
      
      frame = Frame(master)
      #frame.pack()
      self.master = master
      self.master.wm_title("Kruskal")
      self.borrar = Button(master, text="Borrar", fg="red", command=self.limpiar)
      self.borrar.grid(row=0, sticky=E)
      
      self.kruskal = Button(master, text="Kruskal", command=self.drawTree, state=DISABLED)
      self.kruskal.grid(row=0, column=1, sticky=W)
      
      self.canvas = Canvas(master, width=1024, height=800)
      self.canvas.grid(row=1,columnspan=2)
      self.E = []
      self.V = []
      self.clickedVertex = False
      self.canvas.bind("<Button-1>", self.leftclick)
      
   
   def findVertex(self,xf,yf):
      for v in self.V:
         [x,y] = v.getCoords()
         if abs(xf - x) < 7 and abs(yf - y) < 7:
            return v
      return False

   def leftclick(self, event):
      x = int(self.canvas.canvasx(event.x))
      y = int(self.canvas.canvasy(event.y))
      v = self.findVertex(x, y)
      if self.clickedVertex:
         if v:
            d = MyDialog(self.master)
            try:
               p = int(d.result)
               e = Arista(len(self.E), self.clickedVertex, v, p, 0)
               self.E.append(e)
               self.drawEdge(e)
               self.kruskal.config(state=NORMAL)
            except :
               p = None
                  
         self.clickedVertex = False
      else:
         if not v:
            v = Vertice(len(self.V),x,y,0)
            self.V.append(v)
            self.drawVertex(v)
         else:
            self.clickedVertex = v
   
   def drawVertex(self, v):
      self.borrar.config(state=NORMAL)
      [x,y] = v.getCoords()
      self.canvas.create_oval(x-5,y-5,x+5,y+5,fill="blue")
   
   def drawEdge(self,e):
      [v1,v2] = e.getEndpoints()
      [x1,y1] = v1.getCoords()
      [x2,y2] = v2.getCoords()
      m = (y1-y2)/(x1-x2)
      if m < 0:
         anch = "nw"
         off = 3
      else:
         anch = "ne"
         off = -3
      self.canvas.create_text(off+((x2+x1)/2), ((y2+y1)/2)-3, text=str(e.getPeso()),anchor=anch)
      self.canvas.create_line(x1, y1, x2, y2, fill="black")
      
   def drawTree(self):
      T = kruskal(self.E,self.V)
      peso = 0
      for e in T:
         [v1,v2] = e.getEndpoints()
         [x1,y1] = v1.getCoords()
         [x2,y2] = v2.getCoords()
         self.canvas.create_line(x1, y1, x2, y2, fill="magenta",width="2")
         peso += e.getPeso()
      self.kruskal.config(state=DISABLED)
      self.canvas.create_text(4, 4, text="Peso del arbol: "+str(peso),anchor=NW)
   
   def limpiar(self):
      self.canvas.delete(ALL)
      self.borrar.config(state=DISABLED)
      self.E = []
      self.V = []
   


root = Tk()

app = App(root)

root.mainloop()