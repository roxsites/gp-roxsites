from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ProdutoForm

# Create your views here.
@login_required
def produtos_home(request):
    produtos = Produto.objects.all()
    return render(request, 'Produtos_home.html', {'produtos': produtos})

def my_logout(request):
    logout(request)
    return redirect('home')

@login_required
def produto_novo(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('produtos_home')
    return render(request, 'produto_form.html', {'form': form})

@login_required
def produto_atualiza(request, id):
    produto = get_object_or_404(Produto, pk=id)
    form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produtos_home')

    return render(request, 'produto_form.html', {'form': form})

@login_required
def produto_deleta(request, id):
    produto = get_object_or_404(Produto, pk=id)

    if request.method == 'POST':
        produto.delete()
        return redirect('produtos_home')

    return render(request, 'produto_deleta_confirma.html', {'produto': produto} )
