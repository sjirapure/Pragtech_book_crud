from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book
from django.views import View
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class AddBook(LoginRequiredMixin,View):
    template_name = "app1/addbook.html"
    form = BookForm
    
    def get(self,request):
        form  = self.form()
        context ={'form':form}
        return render(request,self.template_name,context)
    def post(self,request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        context ={'form':form}
        return render(request,self.template_name,context)
    
class ShowBook(LoginRequiredMixin,View):
    template_name = 'app1/showbook.html'
    def get(self,request):
        obj = Book.objects.all()
        paginator = Paginator(obj,3)
        try:
            if request.GET.get('page'):
                user = paginator.page(request.GET.get('page'))
            else:
                user = paginator.page(1)
        except EmptyPage:
            user = paginator.page(paginator.num_pages)
        
        context={'obj':user}
        return render(request,self.template_name,context)    
class UpdateBook(LoginRequiredMixin,View):
    template_name = "app1/addbook.html"
    form = BookForm
    
    def get(self,request,id):
        obj = Book.objects.get(id=id)
        form  = self.form(instance=obj)
        context ={'form':form}
        return render(request,self.template_name,context)
    def post(self,request,id):
        obj = Book.objects.get(id=id)
        form = self.form(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        context ={'form':form}
        return render(request,self.template_name,context)
    
        
        
