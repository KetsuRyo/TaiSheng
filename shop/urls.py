
from django.urls import path
from .views.index import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import Checkout, clear_cart
from .views.orders import Orders
from shop.middlewares.auth import auth_middleware
from .views.orders import get_all_orders
from .views.orders import update_order_status
from .views.orders import create_product

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('signup/', Signup.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    path('cart/',auth_middleware(Cart.as_view()), name="cart"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('clear/', clear_cart, name="clear"),
    path('all-orders/', get_all_orders, name='get_all_orders'),
    path('update-order-status/', update_order_status, name='update_order_status'),
    path('create-product/', create_product, name='create_product'),
    path('orders/',auth_middleware( Orders.as_view()), name="orders")
]
