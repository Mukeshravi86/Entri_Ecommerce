
from django.urls import path


from .import views

urlpatterns=[
             
             path("",views.home,name="success"),
             path('acccount/login/',views.login_view,name='login'),
             path('logout',views.logout_view),
             path('accounts/register/',views.register,name='register'),
             path('',views.product_list,name='product_list'),
             path('<int:id>/',views.product_details,name='product_details'),
             path('add',views.add_product,name='add_product'),
             path('<int:id>/edit/',views.edit_product,name='edit_product'),
             path('<int:id>/delete/',views.delete_product,name='delete_product'),
             
             
             ]

