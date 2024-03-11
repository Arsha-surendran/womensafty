"""
URL configuration for scrapbox project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from safeapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.SignUpView.as_view(),name="signup"),

    path("",views.signInView.as_view(),name="signin"),
    path("signout/", views.signoutView.as_view(),name="signout"), 
    path("index/", views.IndexView.as_view(),name="index"),
    path("profile/<int:pk>/change", views.ProfileUpdateView.as_view(),name="profile_edit"),
    path("profile/<int:pk>", views.ProfileDetailView.as_view(), name="profile"),
   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)