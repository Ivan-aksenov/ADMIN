from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>', views.customer, name="customer"),
    path('create_list/',views.createList, name="create_list"),
    path('delete_list/<event_id>',views.deleteList, name="delete_list"),
    path('update_info/<str:pk>', views.Updateinfo, name="update_info"),
    path('delete_info/<str:pk>', views.deleteinfo, name="delete_info"),
]
