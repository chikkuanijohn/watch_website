from django.urls import path
from .views import update_stock
from .views import book_appointment, view_bookings, confirm_order, admin_manage_orders
from .import views


urlpatterns = [
    path('',views.shop_login),
    
    #------------admin------------#
    path('shop_home',views.shop_home),
    path('logout',views.shop_logout),
    path('addproduct', views.addproduct),
    path('edit_product/<pid>',views.edit_product),
    path('delete_product/<pid>',views.delete_product),
    path('add_cate',views.add_category),
    path('view_bookings',views.view_bookings),
    
    
    #------------user--------------#
    path('register/',views.register),
    path('user_home',views.user_home),
    path('contact/', views.contact),
    path('Men',views.Men),
    path('Women',views.Women),
    path('product_view/<pid>',views.product_view),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('cart_pro_buy/<cid>',views.cart_pro_buy),
    path('bookings',views.bookings),
    path('pro_buy/<pid>',views.pro_buy),
    path('qty_in/<cid>',views.qty_in),
    path('qty_dec/<cid>',views.qty_dec),
    path('category_view/<int:category_id>/', views.category_view, name='category_view'),
    path("update_stock/<int:product_id>/", update_stock, name="update_stock"),
    path("update_stock/<int:product_id>/", update_stock, name="update_stock"),
    path("book_appointment/", book_appointment, name="book_appointment"),
    path("view_bookings/", view_bookings, name="view_bookings"),
    path("confirm_order/<int:order_id>/", confirm_order, name="confirm_order"),
    path("admin_orders/", admin_manage_orders, name="admin_orders"),
]