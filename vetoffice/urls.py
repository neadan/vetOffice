from django.urls import path

from . import views

urlpatterns = [
   path("", views.home, name="home"),
   path("owner/list", views.OwnerList.as_view(), name="ownerlist"),
   path("pet/list", views.PetList.as_view(), name="petlist"),
   path("owner/create", views.OwnerCreate.as_view(), name="ownercreate"),
   path("pet/create", views.PetCreate.as_view(), name="petcreate"),
   path("owner/update/<pk>", views.OwnerUpdate.as_view(), name="ownerupdate"),
   path("pet/update/<pk>", views.PetUpdate.as_view(), name="petupdate"),
   path("owner/delete/<pk>", views.OwnerDelete.as_view(), name="ownerdelete"),
   path("pet/delete/<pk>", views.PetDelete.as_view(), name="petdelete")
]