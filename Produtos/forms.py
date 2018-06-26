from django.forms import ModelForm
from .models import Produto


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['produto_nome', 'produto_marca', 'quantidade', 'valor', 'descricao', 'foto']