"""
    Función de procesador de contexto
"""

def importe_total_carro(request):
    total = 0                                                                      # Variable inicializadora de valor
    cantidades = 0                                                                 # Variable inicializadora de cantidad
    if 'carro' not in request.session:
        request.session['carro'] = {}
    if request.user.is_authenticated:                                              # Validación de usuario autenticado
        for key, value in request.session["carro"].items():                        # Recorrido de elementos de la variable de sesión
            total = total + (float(value['precio']) * float(value['cantidad']))    # Calculamos el valor total de los elementos
            cantidades = cantidades + (int(value['cantidad']))                     # Calculamos cuantos articulos tenemos en el carro
    return {'importe_total': total, 'cantidades':cantidades}                       # Retornamos el diccionario de contexto con el dato
