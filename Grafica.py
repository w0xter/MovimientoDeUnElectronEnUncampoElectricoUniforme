import math
import numpy as np
import matplotlib.pyplot as plt
class Electron:
	def __init__(self,posX,posY, velX, velY):
		self.posX  = posX
		self.posY = posY
		self.velX = velX
		self.velY = velY
		self.carga = 1.60*math.pow(10, -19)
		self.masa = -9.11*math.pow(10, -31)

class Grafica:
	def __init__(self,velocidad, angulo):
		self.angulo = math.radians(angulo)
		self.velocidadInicial = velocidad
		velocidadX = self.velocidadInicialX = velocidad * math.cos(self.angulo)
		velocidadY =self.velocidadInicialY = velocidad * math.sin(self.angulo)
		self.electron = Electron(0,0,velocidadX,velocidadY)
		self.campoElectrico = 3.5 * math.pow(10, 3)
		self.aceleracionY = self.campoElectrico * self.electron.carga / self.electron.masa
		self.aceleracionX = 0
		self.atrapado = False
		self.xMax = self.yMax = self.timeXmax = self.timeYmax = None
		self.calcularMaximos()
	def calcularMaximos(self):
		self.timeXmax = -2 * self.velocidadInicialY / self.aceleracionY
		self.xMax = self.velocidadInicialX * self.timeXmax
		self.timeYmax = -1*self.velocidadInicialY / self.aceleracionY
		self.yMax = self.velocidadInicialY * self.timeYmax + self.aceleracionY*math.pow(self.timeYmax, 2)*0.5
		print 'Ymax: ', str(self.yMax), 'Xmax: ', str(self.xMax), 'TimeYMAX', str(self.timeYmax), 'TIMEXMAX', str(self.timeXmax)
	def actualizarPosicion(self):
		if(not self.atrapado):
			self.electron.posX = self.velocidadInicialX * self.time
			self.electron.posY = self.velocidadInicialY*self.time + self.aceleracionY*math.pow(self.time, 2)*0.5
	def actualizarVelocidad(self):
		if(not self.atrapado):
			self.electron.velX = self.velocidadInicialX 
			self.electron.velY = self.velocidadInicialY + self.aceleracionY*self.time
		else:
			self.electron.velX = 0
			self.electron.velY = 0
	def generarDatos(self):
		tope = 0.15
		x = np.arange(0.0,self.xMax , 10**-3)
		y = ((self.velocidadInicialY*x/self.velocidadInicialX) + ((self.aceleracionY * x**2) / (2*self.velocidadInicialX**2)))*1000
		plt.plot(x*1000, y, 'r-o')
		ax = plt.subplot(1,1,1)
		ax.set_ylim(bottom=-0.001, top=self.yMax*1000 + 10)
		ax.text(0,-0.5, '+ + + + + + + + + + + + + + + + + + +', style='normal', color='white',bbox={'facecolor':'blue', 'alpha':0.5, 'pad':0})
		for i in range(6):
			ax.annotate('', xy=(20 * i,25), xytext=(20 * i,5), arrowprops=dict(facecolor='green',alpha=0.5 ,shrink=0, width=2))
		plt.grid(True)
		plt.xlabel('Posicion X mm')
		plt.ylabel('Posicion Y mm')
		plt.show()

#velocidad = float(input("introduce la velocidad Inicial: "))
#angulo = float(input("Introduce el angulo de inicial: "))
grafica  = Grafica(10.10*10**6, 45)
grafica.generarDatos()



