my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list) # Se convierte el iterable en iterador

# print(type(my_iter))


# Extraer los elementos

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


# Esto es lo que hace internamente un ciclo for, el for es azucar sintactica para esconder lo que está pasando por debajo

# Los generadores son formas faciles de crear iteradores, un generador es una función que tiene poderes especiales
# En una función normal cuando se hace un return de un elemento se corta la ejecución de la función, en un generador cuando se hace un return python guarda el estado de la función y continua la ejecución donde lo dejaste, para que cuando se vuelva a llamar a la función ese estado esté disponible

