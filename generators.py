# Los generadores son formas faciles de crear iteradores, un generador es una función que tiene poderes especiales
# En una función normal cuando se hace un return de un elemento se corta la ejecución de la función, en un generador cuando se hace un return python guarda el estado de la función y continua la ejecución donde lo dejaste, para que cuando se vuelva a llamar a la función ese estado esté disponible

def my_func(): 
    a = 1
    return a

    a = 2
    return a

    a = 3
    return a


print(my_func())