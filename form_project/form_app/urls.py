from django.urls import path
from form_app.views import *

urlpatterns = [
    path('',register_view,name='register_view'),
    path('login_view/',login_view,name='login_view'),
    path('dashboard_view/',dashboard_view,name='dashboard_view'),
    path('logout_view/',logout_view,name='logout_view'),

    path('category_list/',category_list,name='category_list'),
    path('add_category/',add_category,name='add_category'),
    path('update_category/<str:id>/',update_category,name='update_category'),
    path('delete_category/<str:id>/',delete_category,name='delete_category'),

    path('add_product/',add_product,name='add_product'),
    path('product_list/',product_list,name='product_list'),
    path('edit_product/<str:p_id>/',edit_product,name='edit_product'),
    path('delete_product/<str:p_id>/',delete_product,name='delete_product'),





]