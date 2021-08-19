#Isebeneador
import os
import buscador as bus
import sqleando as sql
listaisbns=[]

def deconstruirisbns(presibn):
	if len(presibn) >17:
		isbn=presibn[:13]
		if isbn in listaisbns:
			pass
		else:
			listaisbns.append(isbn)
	elif len(presibn) >14:
		isbn=presibn[:10]
		if isbn in listaisbns:
			pass
		else:
			listaisbns.append(isbn)
	else:						
		print(presibn+"<<<<ERROR>>>>")
imagenes=os.listdir("C:/Users/david/Desktop/LIBROS")

emergencia = False

while emergencia==False:
	for f in imagenes:
		deconstruirisbns(f)
	print(listaisbns)
	for l in listaisbns:
		enbase= sql.confirmarenbase(l)
		if enbase == None:
			try:
				resultado=bus.busquedalibro(l)
				print(resultado)
				precio = input("Precio")
				if precio == "Z":
					emergencia=True
					break
				#estado = input("estado I si impecable B si Muy buen estado A aceptable")
				observaciones= input("observaciones")
				tapa = input("Tapa D si Dura o B si Blanda")
				tema = input("tema")
				if tema == "Z":
					emergencia=True
					break
				titulo,autor,editorial,año=resultado	
			except:
				print(l+">>>"+"no existe")
				titulo = input("Titulo")
				autor= input("autor")
				editorial = input("editorial")
				año = input("año")
				precio = input("Precio")
				if precio == "Z":
					emergencia=True
					break
				#estado = input("estado I si impecable B si Muy buen estado A aceptable")
				observaciones= input("observaciones I si impecable B si Muy buen estado ")
				tapa = input("Tapa D si Dura o B si Blanda")
				tema = input("tema")
				if tema == "Z":
					emergencia=True
					break
			if observaciones == "I":
				observaciones = "Impecable"
			elif observaciones == "U":
				observaciones = "Sin uso"	
			if tapa == "D":
				tapa = "Dura"
			elif tapa == "B":
				tapa = "Blanda"
			estado="Usado"							
			datos=(titulo[:49], autor[:30], editorial[:25], año, precio, estado, observaciones, tapa, l, tema)		
			sql.ingresarenbase(datos)
			print(">>>>>>>>>>>>>   GUARDADOR EN LA BASE >>>>>>>>")		
		else:
			print(enbase)
			print("OK")
	emergencia=True		