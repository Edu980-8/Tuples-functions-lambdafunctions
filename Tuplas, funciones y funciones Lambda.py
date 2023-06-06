#!/usr/bin/env python
# coding: utf-8

# In[1]:


tup1 = (1,2,3)
tup2 = (4,5,6)
tup3 = tup1+tup2
tup3


# In[2]:


tup4 = tup1*3


# In[3]:


tup4


# In[4]:


min(tup2)


# In[5]:


max(tup2)


# In[18]:


lista = ["a","b","c","d"]
lista.insert(4,"AA")
print(f"{lista}\n")
lista.append("e")
print(lista)


# In[19]:


lista.sort()


# In[21]:


lista


# In[22]:


lista*3


# In[23]:


lista+lista


# In[24]:


diccionario={"Manzana":3,
            "Pera":5,
            "Banano":10}


# In[25]:


diccionario


# In[26]:


diccionario2 = {"Patata":200}
diccionario.update(diccionario2)
diccionario


# In[27]:


borrado = diccionario.pop("Pera")
borrado


# In[28]:


diccionario


# In[29]:


l1=["apple","banana","orange"]
for i in l1:
    print(i)


# In[31]:


l1 = ["orange","blue","green"]
l2 = ["book","chair","phone"]
for i in l1:
    for j in l2:
        print(i,j)


# In[47]:


number = float(input("Ingrese su numero, la aplicacion le indicará si es par o impar: "))
def even_odd(number):
    if(number%2 == 0):
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")

even_odd(number)    


# In[49]:


number = float(input("Ingrese su numero, la aplicacion le indicará si es positivo, negativo o cero: "))
def neg_pos_zero(number):
    if(number < 0):
        print(f"The number {number} is negative")
    elif (number > 0):
        print(f"The number {number} is positive")
    else:
        print(f"The number is {number}")

neg_pos_zero(number)  


# In[18]:



import math as mt
number = float(input("Ingrese un numero entero, la aplicacion le indicará su factorial: "))
factorial=1
def fact_int_number(number):
    global factorial
    if(number <0):
        print("El factorial no esta definido para numeros negativos")
    elif(number==0):
        print("El factorial de 0 es 1")
    elif ((number%1 != 0) == True):
        factorial = mt.gamma(number) 
        print(f"El factorial  a partir de la funcion gamma es: {factorial}")
    elif(number.is_integer()):
        print(number)
        for i in range(1, int(number)+1):
            factorial = factorial*i
        print(f"El Factorial de {number} es {factorial}")
fact_int_number(number)
    


# In[39]:


number= input("Ingrese su numero entero:")
if (any(number.isdigit() for char in number)):
    number2_str = number[::-1]
    print(f'''El numero original es: {number}\nEl numero al reves es: {number2_str}
          ''')
    number2 = int(number2_str)
    print(type(number2))
    
else:
    print("El valor ingresado no fue un numero entero")
    
def palindromo(number):
    if(number == number[::-1]):
        print("Palindromo!!!!")
    else:
        print("No es palindromo!!!")
palindromo(number)


# In[45]:


g = lambda x:mt.pow(x,3) # g = lambda parametro:operacion
print(g(7))


# In[ ]:




