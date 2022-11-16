#Se pide calcular la nota de tu examen tipo test.
    #Serán 20 preguntas
    #Las preguntas correctas sumarán 0,5
    #Las preguntas incorrectas restarán 0,25
    #Las preguntas sin contestar tendrán 0

#Datos de entrada
    #Respuesta de la pregunta

#Datos de salida
    #La nota total

notaT=0
def nota():
    for pregunta in range(20):
        respuesta=input("Ingrese si su respuesta es correcta: ")
        if respuesta.lower()=="si":
            notaT=notaT+0.5
        if respuesta.lower()=="no":
            notaT=notaT-0.25
        if respuesta.lower()=="":
            notaT=notaT
        print(notaT)
nota()