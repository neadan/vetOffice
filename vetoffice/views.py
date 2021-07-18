from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from vetoffice.models import Owner, Pet


def home(request):
    return render(request, "vetoffice/home.html")


def pets_of_owner(request, name):
    try:
        owner = Owner.objects.get(first_name=name)
    except Owner.DoesNotExist:
        raise Http404(f"There is no owner with the name {name}")

    pets = Pet.objects.filter(owner=owner)
    context = {"pet_list": pets, "owner": owner.first_name}
    return render(request, "vetoffice/pets_of_owner.html", context)


class OwnerList(ListView):
    model = Owner
    template_name = "vetoffice/owner_list.html"


class PetList(ListView):
    model = Pet
    template_name = "vetoffice/pet_list.html"


class OwnerCreate(CreateView):
    model = Owner
    template_name = "vetoffice/owner_create_form.html"
    fields = ["first_name", "last_name", "phone"]

    def get_success_url(self):
        return reverse('ownercreate')


class PetCreate(CreateView):
    model = Pet
    template_name = "vetoffice/pet_create_form.html"
    fields = ["animal_type", "breed", "name", "age", "owner"]

    def get_success_url(self):
        return reverse('petcreate')


class OwnerUpdate(UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    fields = ["first_name", "last_name", "phone"]

    def get_success_url(self):
        return reverse('ownerlist')


class PetUpdate(UpdateView):
    model = Pet
    template_name = "vetoffice/pet_update_form.html"
    fields = ["animal_type", "breed", "name", "age", "owner"]

    def get_success_url(self):
        return reverse('petlist')


class OwnerDelete(DeleteView):
    model = Owner
    template_name = "vetoffice/owner_delete_form.html"

    def get_success_url(self):
        return reverse('ownerlist')


class PetDelete(DeleteView):
    model = Pet
    template_name = "vetoffice/pet_delete_form.html"

    def get_success_url(self):
        return reverse('petlist')