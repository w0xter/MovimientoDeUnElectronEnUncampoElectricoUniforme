import math
import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
import matplotlib.patches as patches
from decimal import Decimal
#Realizado por Luis Pozo Gilo Grupo GM11 ingenieria de software.
#Lenguaje de programacion Python 2.
#Al final del documento adjunto una hoja con las formulas utilizadas, mejor explicadas.
#No hay tildes en el documento debido a posibles incompatibilidades a la hora de compilar.
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)#Irrelevante, era solo para que no saltase un aviso cada vez que se ejecutase el programa.
class Grafica:
	def __init__(self,velocidad, angulo):
		self.angulo = math.radians(angulo)
		self.velocidadInicial = velocidad
		velocidadX = self.velocidadInicialX = velocidad * math.cos(self.angulo)
		velocidadY =self.velocidadInicialY = velocidad * math.sin(self.angulo)
		self.campoElectrico = 3.5 * 10**3
		self.masa = 9.11*10**-31#Masa electron
		self.carga = -1.60*10**-19#Carga Electron
		self.aceleracionY = self.campoElectrico * self.carga / self.masa
		self.aceleracionX = 0
		self.distanciaMaxX =self.distanciaMaxY =self.alturaMaxX = self.alturaMaxY = self.timeDistanciaMax = self.timeAlturaMax = 0
		self.calcularMaximos()
	def calcularMaximos(self):
		self.timeDistanciaMax = -2 * self.velocidadInicialY / self.aceleracionY#Calculamos la distancia maxima utilizando el tiempo que tarda en hacerse 0  la componente "Y" de la posicion del electron.
		self.distanciaMaxX = self.velocidadInicialX * self.timeDistanciaMax
		self.distanciaMaxY = 0
		self.timeAlturaMax = -1*self.velocidadInicialY / self.aceleracionY#Calculamos la altura maxima con el tiempo que tarda hacerse la componente "Y" de la velocidad del electron 0
		self.alturaMaxY = self.velocidadInicialY * self.timeAlturaMax + self.aceleracionY*(self.timeAlturaMax**2)*0.5
		self.alturaMaxX = self.velocidadInicialX *self.timeAlturaMax
	def toStringDistancia(self):
		x = '%.2E' % Decimal(self.distanciaMaxX)
		mensaje = 'El electron no queda\natrapado en el Campo Electrico.'
		if (self.distanciaMaxX <= 0.10):
			mensaje = str('Distancia Maxima: '+ str(x) + ' metros.')
		return mensaje
	def toStringAltura(self):
		y = 'El lectron no queda\natrapado en el campo Electrico.'
		if(self.alturaMaxX <= 0.10):
			y = str('Altura Maxima: ' + str('%.2E' % Decimal(self.alturaMaxY)) + ' metros')
		return y
	def toStringCampoElectrico(self):
		campo = '%.2E'% Decimal(self.campoElectrico)
		return str('E: ' + campo + ' N/C.')
	def toStringInputs(self):
		velocidad = str('%.2E' % Decimal(self.velocidadInicial))
		angulo = str(math.degrees(self.angulo))
		return str('Velocidad inicial : ' + velocidad + ' m/s.\n' + 'Angulo Inicial: ' + angulo +' Grados.')
	def f(self,x):
		y = ((self.velocidadInicialY*x/self.velocidadInicialX) + ((self.aceleracionY * x**2) / (2*self.velocidadInicialX**2)))#Graficamos el recorrido del electron combinando las ecuaciones del mrua para obtener las posiciones X e Y (Mejor explicado Abajo).
		y = y * 10**3
		return y
	def generarDatos(self):
		tope = 0.15 #Distancia suficiente como para conocer si el electron queda atrapado en el CampoElectrico o no.
		if self.distanciaMaxX < 0.10:#Si el Electron quedase atrapado dentro del campo Electrico solo se mostraria la funcion hasta el punto f(x) = 0
			tope = self.distanciaMaxX
		x = np.linspace(0,tope) #Rango de x
		plt.plot(x*1000,self.f(x),'r')#Generamos la grafica, x queda multiplicado por 1000 para obtener la grafica en milimetros.
		ax = plt.subplot(1,1,1) # Generamos unos nuevos ejes para poder mostrar solo la parte de la grafica que nos interesa.
		ax.set_ylim(bottom=-5, top=120)
		ax.set_xlim(left =-5, right=120)
		cargasPositivas = patches.Rectangle((0,-5), 100, 5, fill=True, facecolor='green')#Representamos donde se encuentran situadas las cargas positivas.
		leyendaCargasPositivas = patches.Patch(color='green', label='Cargas Positivas')
		leyendaDistanciaMaxima = patches.Patch(color='black',label=self.toStringDistancia())
		leyendaCampoElectrico = patches.Patch(color='yellow', label=self.toStringCampoElectrico())
		leyendaAlturaMaxima = patches.Patch(color='orange', label=self.toStringAltura())
		leyendaInputs = patches.Patch(color = 'blue', label=self.toStringInputs())
		leyendaRecorrido = patches.Patch(color='red', label='Trayectoria del electron\nsegun los valores anteriores')
		plt.legend(handles=[leyendaCargasPositivas, leyendaCampoElectrico, leyendaDistanciaMaxima, leyendaAlturaMaxima, leyendaInputs, leyendaRecorrido])
		ax.add_patch(cargasPositivas)
		ax.annotate('', xy=(math.cos(self.angulo)*50, math.sin(self.angulo)*50), xytext=(0,0), arrowprops=dict(arrowstyle='->',color='blue', connectionstyle='arc3'))#Representamos la direccion de la velocidad Inicial del electron.
		for i in range(8):
			ax.annotate('', xy=(15 + 10 * i,85), xytext=(15 + 10 * i,25), arrowprops=dict(color='yellow', arrowstyle='->'))#Generamos 8 flechas para representar el CampoElectrico y su direccion.
		plt.grid(True)
		plt.xlabel('Posicion X mm')
		plt.ylabel('Posicion Y mm')
		plt.title('Movimiento de un electron con una velocidad inicial\na traves de un campo electrico.')
		plt.show()

def leerDatos():
	angulo = float(input("Introduce el Angulo incial: "))
	exponente = 0
	print 'Ejemplo: 3.5*10^6 -> Coeficiente = 3.5, exponente = 6'
	coeficiente = float(input("Introduce el coeficiente: "))
	exponente = int(input("Introduce el exponente: "))
	velocidad = coeficiente * 10**exponente
	return velocidad, angulo
velocidad, angulo = leerDatos()
grafica  = Grafica(velocidad, angulo)
grafica.generarDatos()



