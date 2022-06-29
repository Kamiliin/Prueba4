from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import CustomUser, Product, Category
from .forms import CategoryDeleteForm, ProductDeleteForm, UserForm, ProductForm, CategoryForm
from django.urls.base import reverse, reverse_lazy
# Create your views here.

def index(request, template_name="home.html"):
    response = render(request, template_name)
    return response

class CreateUserView(CreateView):
    model = CustomUser
    form_class = UserForm
    template_name = 'users/create_user.html'
    success_url = reverse_lazy('home')

class DogStoreView(TemplateView):
    template_name = 'store/dog_store.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context

class CatStoreView(TemplateView):
    template_name = 'store/cat_store.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context

class ListProductsView(ListView):
    model = Product
    template_name = 'products/list_products.html'
    queryset = Product.objects.all().order_by("id")

class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create_product.html'
    success_url = reverse_lazy('list_products')


class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/edit_product.html'
    success_url = reverse_lazy('list_products')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('list_products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in kwargs:
            context['form'] = ProductDeleteForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ProductDeleteForm(request.POST, instance=self.object)
        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )
    
class ListCategoriesView(ListView):
    model = Category
    template_name = 'categories/list_categories.html'
    queryset = Category.objects.all().order_by("id")

class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('list_categories')

class EditCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/edit_category.html'
    success_url = reverse_lazy('list_categories')

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'categories/delete_category.html'
    success_url = reverse_lazy('list_categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in kwargs:
            context['form'] = CategoryDeleteForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CategoryDeleteForm(request.POST, instance=self.object)
        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.render_to_response(
                self.get_context_data(form=form)
            )
    
