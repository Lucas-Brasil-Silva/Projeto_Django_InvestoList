from django.contrib import admin
from django.urls import path
from invista_me import views
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/', usuarios_views.novo_usuario,name='novo_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/logout.html'),name='logout'),
    path('novo_investimento/', views.criar,name='novo_investimento'),
    path('', views.investimento,name='investimento'),
    path('Quit/', views.investimento,name='quit'),
    path('<int:id_investimento>/',views.detalhe,name='detalhe'),
    path('novo_investimento/<int:id_investimento>/', views.editar,name='editar'),
    path('deletar/<int:id_investimento>/',views.deletar,name='deletar')
]