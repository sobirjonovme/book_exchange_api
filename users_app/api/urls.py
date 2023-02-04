from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # For Token Authentication

from users_app.api import views as users_views

app_name = 'users'

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', users_views.RegistrationAPIView.as_view(), name='register'),
    path('logout/', users_views.LogOutAPIView.as_view(), name='logout'),

]
