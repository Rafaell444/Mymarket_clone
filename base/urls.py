from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
                  path("login/", views.loginPage, name="login"),
                  path("logout/", views.logoutPage, name="logout"),
                  path("register/", views.registerPage, name="register"),

                  path('', views.home, name="home"),
                  path('product/<str:pk>/', views.product, name="product"),

                  path('create_product/', views.createproduct, name="create_product"),
                  path('update_product/<str:pk>/', views.updateproduct, name="update_product"),
                  path('delete_product/<str:pk>/', views.deleteproduct, name="delete_product"),

                  path('profile/<str:pk>/', views.profilepage, name="profile"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
