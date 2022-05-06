from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<str:pk>/', views.product, name="product"),

    path('create_product/', views.createproduct, name="create_product"),
    path('update_product/<str:pk>/', views.updateproduct, name="update_product"),
    path('delete_product/<str:pk>/', views.deleteproduct, name="delete_product")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
