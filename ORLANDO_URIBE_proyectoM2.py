#el usuario debe crear una palabra con minimo 4 caracteres y un maximo de 8
#declaramos variables:
palabra = ""
caracteres= ""
#comenzamos ciclo:
while True:
  palabra = input("Escriba una palabra entre 4 y 8 caracteres: ")#pedimos al usuario la palabra
  caracteres = len(palabra)#medimos la longitud de la palabra y la guardamos en la variable caracteres
  if caracteres < 4:#condicionamos que la palabra no tenga menos de 4 caracteres
     print("longitud corta: contiene " + str (len(palabra)) + " caracteres")#imprimimos el mensaje en caso de que la condicion no se cumpla
  elif caracteres > 8:#condicionbamos que la palabra no tenga mas de 8 caracteres
     print("longitud larga: contiene " + str (len(palabra))+ " caracteres")#imprimimos el mensaje en caso de que la condicon no se cumpla
  else:
     print("la palabra es correcta")#imprimimos cuando las 2 condiciones se cumplan
     break#cierre de ciclo cuando las 2 coniciones se cumplan


#cuadrante en el plano carteciano

#comenzamos ciclo:

while True:#inicamos el ciclo que sea verdadero
   x=(int)(input("Escriba la cordenada x: "))#le pedimos al usuario la cordenada "x"
   y=(int)(input("Escriba la cordenada y: "))#le pedimos al usuario la cordenada"y"
   if (x==0) or (y==0):#comprobamos que los dos valores no esten en "0"
      print("Las cordenadas no pueden quedar en 0")#le decimos al usuario que las cordenadas no pueden quedar en "0"
   elif (x>0) and (y>0):#evaluamos que las dos cordenadas queden positivas
      print("sus cordenadas en ecuadrtante I")#le decimos al usuario en que ciuadrante estan sus cordenadas
      break#salimos del ciclo si estan bien las cordenadas en positivo
   elif (x<0) and (y>0):#evaluamos que la cordenada"x" este en negativo y la cordenada "y" este en positivo
      print("sus cordenadas en ecuadrtante II")#le decimos al usuario en que ciuadrante estan sus cordenadas
      break#salimos del ciclo si la cordenada "x" esta en negativo
   elif (x>0) and (y<0):#evaluamos que la cordenada"y" este en negativo y la cordenada "x" este en positivo
      print("sus cordenadas en ecuadrtante IV")#le decimos al usuario en que ciuadrante estan sus cordenadas
      break#salimos del ciclo si la cordenada "y" esta en negativo
   elif (x<0) and (y<0):#evaluamos que las dos cordenadas queden negativas
      print("sus cordenadas en ecuadrtante III")#le decimos al usuario en que ciuadrante estan sus cordenadas
      break#salimos del ciclo si estan bien las cordenadas en negativo
      
      

      

   

    


