from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.imovel_form, name='imovel_cadastro'),
	path('<int:id>', views.imovel_form, name='imovel_update'),
	path('delete/<int:id>', views.imovel_delete, name='imovel_delete'),
	path('list/', views.imovel_list, name='imovel_list')
]