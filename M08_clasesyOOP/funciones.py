class Funciones:
    def __init__(self, lista1):
        self.lista1=lista1

    def es_primo(self):
        for i in self.lista1:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def convertir_temperatura(self, origen, destino):
        for i in self.lista1:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)
    
    def factorial(self):
        for i in self.lista1:
            print('El factorial de ', i, 'es', self.__factorial(i))

    def __verifica_primo(self,n):
        primo=True
        for div in range(2,n):
            if n%div==0:
                primo=False
                break            
        return primo
    def ver_moda(self,lista_numeros):
        lista_unicos=[]
        lista_repeticiones=[]
        if len(lista_numeros) == 0:
            return None
        for elementos in lista_numeros:
            if elementos in lista_unicos:
                indice = lista_unicos.index(elementos)
                lista_repeticiones[indice] += 1
            else:
                lista_unicos.append(elementos)
                lista_repeticiones.append(1)

        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]

        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]

        return moda, maximo
    
    def __conversion_grados(self,num, medida_origen, medida_destino):
        if medida_origen=='celsius':
            if medida_destino=='farenheit':
                celsius_farenheit = (num * 9/5) + 32
                return celsius_farenheit
                print(f'{num}°C= {celsius_farenheit}°F')
            if medida_destino=='kelvin':
                celsius_kelvin = num + 273.15
                return celsius_kelvin
                print(f'{num}°C = {celsius_kelvin}°K')
        if medida_origen=='farenheit':
            if medida_destino=='celsius':
                farenheit_celsius = (num - 32) * 5/9
                return farenheit_celsius
                print(f'{num}°F = {farenheit_celsius}°C')
            if medida_destino=='kelvin':
                farenheit_kelvin = ((num - 32) * 5/9) + 273.15
                return farenheit_kelvin
                print(f'{num}|F = {farenheit_kelvin}°K')
        if medida_origen=='kelvin':
            if medida_destino=='celsius':        
                kelvin_celsius = num - 273.15
                return kelvin_celsius
                print(f'{num}°K = {kelvin_celsius}°C')
            if medida_destino=='farenheit':
                kelvin_farenheit = ((num - 273.15) * 9/5) + 32
                return kelvin_farenheit
                print(f'{num}°K = {kelvin_farenheit}°F')
    def __factorial(self,num):
        if num<0:
            return'El número debe ser positivo'
        if type(num)!=int:
            return'El número debe ser entero'
        if num<=1:
            return 1
        
        num=num*self.__factorial(num-1)
        return num