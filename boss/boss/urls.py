from django.contrib import admin
from django.urls import path, include
from page.views import index, create_call
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create_call/', create_call, name='create_call'),
    path('', index, name='index')
]
