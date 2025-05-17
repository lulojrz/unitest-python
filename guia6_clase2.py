def volumen_esfera(radio:float) -> float:
    #aproximamos pi a 3,14
    res: float = 4/3 * 3.14 * radio**3
    return res


def triada_pitagorica(a: int, b: int, c:int) -> bool:
    suma: int = a**2 + b**2
    res: bool = suma == c**2
    return res

def suma(x:int,y:int)-> int : 
    res:int = x+y
    return res
   

def esMultiplo(x:int,y:int) -> bool :
     res : int = x%y 
     return (res==0)


def  fahrenheit_a_celsius (temp:int)-> float:
  
  return  (((temp-32)*5)/9)  
 

def devolver_el_doble_si_es_par(num:int)->int:
  if(num%2==0):
    return num*2

  else:
    return num

def es_primo(num:int)-> bool:

    resultado= True

    if(num<2):
       resultado= False
    else : 
       for divisor in range(2,num,1):
          if esMultiplo(num,divisor):
             resultado= False
 
       

    return resultado

def cuanto_primos_enrango(x:int,y:int)->int:
   contador = 0
   if(x>y) :
      menor = y
      mayor=x
   else:
      menor= x
      mayor = y

   for numero in range(menor,mayor+1):
      if (es_primo(numero)):
         contador+=1


   return contador