#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import os
import time

class modulo:
   nombreModulo = ""
   archivoModulo = ""
   dic_comandos = {"1":"P0","2":"","3":"","4":"P2","5":"","6":"","7":"P1","8":"","9":"D8","10":"","11":"D4","12":"","13":"","14":"","15":"D5","16":"D6","17":"D3","18":"D2","19":"D1","20":"D0"}
  # pinescargados = [] #Es posible que así esté mal instanciado
   
   
   def __init__(self):
     while True:
       try:
	 self.nombreModulo = raw_input("Nombre del módulo>")
       except EOFError: #EOF
	 print "--Saliendo del programa--"
	 sys.exit(1)
       if len(self.nombreModulo) == 0:
	   continue
       self.pinescargados = {}    # crea una nueva lista vacía para cada modulo
       self.dicpines_str = {}	# además de otra para la copia en formato str.
       
       self.dicdispositivos = {}	# diccionario en el que guardar el nombre de cada actuador
       self.dicpines_asignados = {}	# diccionario en el que guardar la asociacion nombre-pin
       break
     
   def cargar(self):
     self.archivoModulo = self.nombreModulo
     self.archivoModulo += ".json"
     print "Nombre del archivo json del que cargar la configuración: {}".format(self.archivoModulo)
     try:
       with open(self.archivoModulo) as f:
	 self.pinescargados = json.load(f)
     except IOError:
       print "El módulo indicado no dispone de fichero de configuración, inicialícelo primero"
       sys.exit(1)
     #print "Pines cargados: {}".format(self.pinescargados)
     #Se muestran "u" que significan unicode, no tiene importancia. (CREO)
     #Aún así, se crea una copia en dicpines_str con el diccionario en formato str.
     
   def to_str(self, data):
     nuevodicpines = {}
     for key, value in data.iteritems():
       if isinstance(key, unicode):
	 key = str(key)
       if isinstance(value, unicode):
	 value = str(value)
       nuevodicpines[key] = value
     self.dicpines_str = nuevodicpines
     print "Pines cargados convertidos a str: {}".format(self.dicpines_str)
     return data
   
   def nombrar(self):
     for k, v in self.dicpines_str.iteritems():
       if v != "":
	 try:
	   nombreDisp = raw_input("En el pin {} hay un {}. Distinguir como:>".format(k, v))
	 except EOFError:
	   print "--Saliendo del programa--"
	   sys.exit(1)
	 else:
	   self.dicpines_asignados[nombreDisp] = k	#guardar el pin
	   self.dicdispositivos[nombreDisp] = v		#guardar el tipo de dispositivo
       else:
	 print "Pin {} no asignado".format(k)
     print "---Nombre y clase de cada dispositivo:---\n {}\n".format(self.dicdispositivos)
   
   def f_actuadores(self, nombre):
     while True:
      print "1-Activar actuador \n2-Activar actuador durante cierto tiempo \n3-Desactivar el actuador"
      try:
	opt = raw_input("Opción>")
      except EOFError:
	print "--Saliendo del programa--"
	sys.exit(1)
      if len(opt) == 0:
	continue
      if opt == "1":
	print "Activando actuador.\n"
      elif opt == "2":
	print "Activando actuador durante cierto tiempo\n"
      elif opt == "3":
	print "Desactivando el actuador\n"
      else:
	print "Opción no válida. Opciones válidas: 1 -- 2 -- 3"
	continue
      print "El pin sobre el que se actuará será el {}\n".format(self.dicpines_asignados[nombre])
      pin_actual = self.dicpines_asignados[nombre]
      if self.dic_comandos[pin_actual] != "":
	print "Por tanto, el comando utilizado será {}\n".format(self.dic_comandos[pin_actual])
      else:
	print "ERROR: No existe comando para trabajar sobre este pin"
      break
     
   def f_indicadores(self, nombre):
     while True:
      print "1-Activar indicador \n2-Activar durante cierto tiempo \n3-Activar con un tipo de parpadeo (tiempo apagado/tiempo encendido) \n4-Desactivar"
      try:
	opt = raw_input("Opción>")
      except EOFError:
	print "--Saliendo del programa--"
	sys.exit(1)
      if len(opt) == 0:
	continue
      if opt == "1":
	print "Activando indicador.\n"
      elif opt == "2":
	print "Activando indicador durante cierto tiempo\n"
      elif opt == "3":
	print "Parpadeo\n"
      elif opt == "4":
	print "Desactivando el indicador\n"
      else:
	print "Opción no válida. Opciones válidas: 1 -- 2 -- 3 -- 4"
	continue
      print "El pin sobre el que se actuará será el {}\n".format(self.dicpines_asignados[nombre])
      pin_actual = self.dicpines_asignados[nombre]
      if self.dic_comandos[pin_actual] != "":
	print "Por tanto, el comando utilizado será {}\n".format(self.dic_comandos[pin_actual])
      else:
	print "ERROR: No existe comando para trabajar sobre este pin"
      break
    
   def f_pulsadores(self, nombre):
     while True:
      print "Defina que quiere hacer para: \n1-Evento pulsación simple \n2-Evento pulsación doble \n3-Evento pulsación larga \n4-Evento pulsación muy larga"
      try:
	opt = raw_input("Opción>")
      except EOFError:
	print "--Saliendo del programa--"
	sys.exit(1)
      if len(opt) == 0:
	continue
      if opt == "1":
	print "Evento pulsación simple\n"		#Pedir variable (dispositivo)
      elif opt == "2":
	print "Evento pulsación doble\n"		#Pedir variable (dispositivo)
      elif opt == "3":
	print "Evento pulsación larga\n"		#Pedir variable (dispositivo)
      elif opt == "4":
	print "Evento pulsación muy larga\n"		#Pedir variable (dispositivo)
      else:
	print "Opción no válida. Opciones válidas: 1 -- 2 -- 3 -- 4" 
	continue
      print "El pin sobre el que se actuará será el {}\n".format(self.dicpines_asignados[nombre])
      pin_actual = self.dicpines_asignados[nombre]
      if self.dic_comandos[pin_actual] != "":
	print "Por tanto, el comando utilizado será {}\n".format(self.dic_comandos[pin_actual])
      else:
	print "ERROR: No existe comando para trabajar sobre este pin"
      break
    
   def f_analogicos(self, nombre):
     while True:
      print "1-Fijar umbrales mínimo y máximo \n2-Fijar histéresis \n3-Evento zona mínima \n4-Evento zona máxima \n5-Evento zona media"
      try:
	opt = raw_input("Opción>")
      except EOFError:
	print "--Saliendo del programa--"
	sys.exit(1)
      if len(opt) == 0:
	continue
      if opt == "1":
	print "Fijando umbrales.\n"	#Pedir variable (valor actual potenciometro)
      elif opt == "2":
	print "Fijando histeresis\n"	#Pedir variable (valor actual potenciometro)
      elif opt == "3":
	print "Defina evento de zona minima\n"	#Pedir variable (dispositivo)
      elif opt == "4":
	print "Defina evento de zona maxima\n"	#Pedir variable (dispositivo) 
      elif opt == "5":
	print "Defina evento de zona media\n"	#Pedir variable (dispositivo)
      else:
	print "Opción no válida. Opciones válidas: 1 -- 2 -- 3 -- 4 -- 5"
	continue
      print "El pin sobre el que se actuará será el {}\n".format(self.dicpines_asignados[nombre])
      pin_actual = self.dicpines_asignados[nombre]
      if self.dic_comandos[pin_actual] != "":
	print "Por tanto, el comando utilizado será {}\n".format(self.dic_comandos[pin_actual])
      else:
	print "ERROR: No existe comando para trabajar sobre este pin"
      break
    
   # Mapear las opciones con su bloque de funcion
   dic_options = {"Actuador" : f_actuadores,
           "Indicador" : f_indicadores,
           "Pulsador" : f_pulsadores,
           "Analogico" : f_analogicos
   }

####################################################################
## Programa principal
if __name__ == "__main__":
  device = modulo()
  
  device.cargar()
  
  device.to_str(device.pinescargados)	#Necesario convertir los valores en string para mejor manejo
  
  device.nombrar()

  while True:
    try:
      interactuado = raw_input("Nombre del dispositivo con el que interactuar>")
    except EOFError:
      print "--Saliendo del programa--"
      sys.exit(1)
    if len(interactuado) == 0:
      continue
    
    if device.dicdispositivos.has_key(interactuado):
      print "El dispositivo '{}' es un {}.\n".format(interactuado, device.dicdispositivos[interactuado])
    else:
      print "El nombre de dispositivo indicado no existe, pruebe otra vez\n"
      continue
    print "Para el dispositivo '{}' existen las siguientes acciones:".format(interactuado)
    tipo_actual = device.dicdispositivos[interactuado]
    device.dic_options[tipo_actual](device, interactuado)
    try:
      com = raw_input("Comando a enviar>")
    except EOFError:
      print "--Saliendo del programa--"
      sys.exit(1)
    if len(com) == 0:
      continue
    
    #SIGUIENTE: Incorporar comando final a enviar -> Ejem: E15:D01
