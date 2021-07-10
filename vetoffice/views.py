from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from vetoffice.models import Owner, Pet


def home(request):
    try:
        p_key = 10
        found_pet = Pet.objects.get(pk=p_key)
    except Pet.DoesNotExist:
        raise Http404(f"There was no pet found with pk={p_key}")

    context = {"name": "Djangoer", "pet": found_pet}
    return render(request, "vetoffice/home.html", context)


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