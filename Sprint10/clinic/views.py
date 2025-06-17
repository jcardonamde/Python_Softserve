from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'clinic/home.html')

def services(request):
    return render(request, 'clinic/services.html')

def placeholder(request):
    # Ejemplo de contexto dinámico mínimo
    context = {
        'items': ['Mascotas', 'Citas', 'Dueños']
    }
    return render(request, 'clinic/placeholder.html', context)