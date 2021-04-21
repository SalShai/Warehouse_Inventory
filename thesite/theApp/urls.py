from django.urls import path

from . import views

urlpatterns = [
    path('',views.viewInventory, name='Inv'),
    path('formProduct',views.formProduct, name='formP'),
    path('addProduct',views.addProduct, name='addP'),
    path('viewProduct',views.viewProduct, name='viewP'),
    path('formLocation',views.formLocation, name='formP'),
    path('addLocation',views.addLocation, name='addL'),
    path('viewLocation',views.viewLocation, name='viewL'),
    path('formProductMove/<int:P>',views.formProductMove, name='ProdMov'),
    path('moveHis',views.Movement ,name='move'),
    path('movementHistory',views.viewHistoty ,name='His')
]