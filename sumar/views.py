from django.shortcuts import render

def sumar_view(request):
    resultado = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            res = num1 + num2
            
            # Si el resultado es un número entero (ej: 6.0), lo convertimos a int para quitar el .0
            if res.is_integer():
                resultado = int(res)
            else:
                resultado = res
                
        except ValueError:
            resultado = "Por favor ingresa números válidos"
            
    return render(request, 'sumar/sumar.html', {'resultado': resultado})