"""FinalBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs import views as blogs_views
from users import views as users_views
from blogs.views import BlogCreateView,BlogListView,BlogDetailView,BlogUpdateView,BlogDeleteView

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',blogs_views.index,name="index"),
    path('post/create/',BlogCreateView.as_view(),name="create"),
    path('post/list/',BlogListView.as_view(),name="list"),
    path('post/detail/<int:pk>/',BlogDetailView.as_view(),name="detail"),
    path('post/<int:pk>/update/',BlogUpdateView.as_view(),name="update"),
    path('post/<int:pk>/delete/',BlogDeleteView.as_view(),name="delete"),
    path('user/register/',users_views.register,name="register"),
    path('user/login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('user/logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="logout"),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
