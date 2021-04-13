from django.urls import path, re_path, include
from . import views
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView, LogoutView
# from rest_framework.routers import DefaultRouter
# from .api import UserViewSet, ProfilViewSet, FieldViewSet, CompetenceViewSet
# # from .views import PasswordsChangeView
# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'profils', ProfilViewSet, basename='profil')  
# router.register(r'fields', FieldViewSet, basename='field')
# router.register(r'competences', CompetenceViewSet, basename='competence')
app_name = 'matrice'

urlpatterns = [
    # path('api/', include(router.urls)),
    # path('Connexion/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='Connexion'),
    # path('Deconnexion/', auth_views.LogoutView.as_view(next_page='matrice:Connexion',template_name='registration/logout.html'), name='Deconnexion'),
    # path('mot_de_passe/', views.change_password, name='change_password'),
    path('', views.index, name='index'),
    path('Enregistrement/', views.register, name='Enregistrement'),

]