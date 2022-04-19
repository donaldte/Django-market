from django.urls import path
from boutique import views

app_name = 'boutique'
urlpatterns = [
    path('', views.store, name='store'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
]
