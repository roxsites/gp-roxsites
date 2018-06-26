from django.urls import path
from .views import produtos_home, my_logout, produto_novo, produto_atualiza, produto_deleta


urlpatterns = [
    path('', produtos_home, name="produtos_home"),
    path('logout/', my_logout, name="logout"),
    path('novo/', produto_novo, name="produto_novo"),
    path('atualizar/<int:id>/', produto_atualiza, name="produto_atualiza"),
    path('deletar/<int:id>/', produto_deleta, name="produto_deleta"),

]