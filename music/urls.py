"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
	# music/
	path('', views.IndexView.as_view(), name='index'),
	# music/register
	path('register/', views.UserFormView.as_view(), name='register'),
	# music/pk
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# music/album/add
	path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
	# music/album/pk
	path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album-update'),
	#music/album/pk/delete
	path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),
	# accounts/....
	path('accounts/', include('django.contrib.auth.urls')),  # user authentication
]

#accounts/login/ [name='login']
#accounts/logout/ [name='logout']
#accounts/password_change/ [name='password_change']
#accounts/password_change/done/ [name='password_change_done']
#accounts/password_reset/ [name='password_reset']
#accounts/password_reset/done/ [name='password_reset_done']
#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']
