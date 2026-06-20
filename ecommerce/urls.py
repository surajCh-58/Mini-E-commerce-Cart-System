from django.urls import path
from . import views

urlpatterns = [
    path('insert',views.InsertEdit,name="insert"),
    path('edit/<int:pk>/',views.InsertEdit,name="edit"),
    path('delete/<int:pk>/',views.Delete,name="delete"),
    path('addcategory',views.Addcategory,name="addcategory"),
    path('editcategory/<int:pk>/',views.Addcategory,name="editcategory"),
    path('deletecatgeory/<int:pk>/',views.DeleteCategory,name="deletecategory"),
    path('allproduct',views.AllProduct,name="allproduct"),
    path('allcategory',views.AllCategory,name="allcategory")
]
