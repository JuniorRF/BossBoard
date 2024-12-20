from django.contrib import admin
from django.urls import path, include
from page.views import index, delete_call, edit_call
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('delete-call/<int:call_id>/', delete_call, name='delete-call'),
    path('edit_call/<int:call_id>/', delete_call, name='edit_call'),
]
