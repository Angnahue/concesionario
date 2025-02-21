from django.shortcuts import render, redirect
from .forms import ClienteForm, ModeloDeAutoForm, VendedorForm, BuscarModeloForm
from .models import ModeloDeAuto

def home(request):
    return render(request, 'app_concesionario/home.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    return render(request, 'app_concesionario/crear_cliente.html', {'form': form})

def crear_modelo(request):
    if request.method == 'POST':
        form = ModeloDeAutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ModeloDeAutoForm()
    return render(request, 'app_concesionario/crear_modelo.html', {'form': form})

def crear_vendedor(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VendedorForm()
    return render(request, 'app_concesionario/crear_vendedor.html', {'form': form})

def buscar_modelo(request):
    form = BuscarModeloForm(request.GET or None)
    resultados = None
    if form.is_valid():
        consulta = form.cleaned_data.get('consulta')
        resultados = ModeloDeAuto.objects.filter(modelo__icontains=consulta)
    return render(request, 'app_concesionario/buscar_modelo.html', {'form': form, 'resultados': resultados})
