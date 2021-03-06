from django.urls import path, include
from authentication import views

app_name = 'authentication'

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('login_party/', views.login_party, name='login_party'),
    path('logout/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('register_party/', views.register_party, name='register_party'),
    path('group/', include('group.urls'))
]
