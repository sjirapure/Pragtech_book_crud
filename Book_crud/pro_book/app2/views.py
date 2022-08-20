from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.views import View
# Create your views here.

class RegisterUser(View):
     template_name = 'app2/register.html'
     form  = UserCreationForm
     def get(self,request):
         form  = self.form()
         context ={'form':form}
         return render(request,self.template_name,context)
     def post(self,request):
         form = self.form(request.POST)
         if form.is_valid():
             form.save()
             return redirect('login_url')
         context={'form':form}
         return render(request,self.template_name,context)      
     
     
class LoginUser(View):
    template_name= 'app2/login.html'
    def get(self,request):
        context={}
        return render(request,self.template_name,context) 
    def post(self,request):
        un = request.POST.get('u')
        pw = request.POST.get('p')
        user = authenticate(username = un , password = pw)
        if user is not None:
            login(request,user)
            return redirect ('show_url')
        context={}
        return render(request,self.template_name,context)
    
class LogoutUser(View):
    def get(self,request):
        logout(request)
        return redirect('login_url')     
        
        



    