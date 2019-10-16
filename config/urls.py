from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from users import views as user_views
from knuckledragger.views import lobby
import knuckledragger.views

admin.autodiscover()

urlpatterns = [
    path('account/', user_views.account, name='account'),
    path("", knuckledragger.views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("test/", knuckledragger.views.test, name="test-room"),
    path("lobby/", login_required(lobby.as_view()), name="lobby"),
    path("admin/", admin.site.urls),
    path('register/', user_views.register, name='register'),
]
