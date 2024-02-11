from django.shortcuts import render, redirect
from django.contrib.auth.models import  User, auth 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect("/")
        
        else:
            form = AuthenticationForm(request)
            return redirect("login")
            
    else:
        context = {
            "form": form
        }    
        return render(request, "accounts/login.html", context)

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
        
#         user = auth.authenticate(username=username, password=password)
        
#         if user is not None:
#             auth.login(request, user)
#             return redirect("/")
        
#         else:
#             context = {
#                 "error": "Invalid login credentials"
#             }
#             return redirect("login")
            
#     else:
#         context = {
#             "error": ""
#         }    
#         return render(request, "accounts/login.html", context)

def logout_view(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("login")
    
    else:
        return render(request, "accounts/logout.html")

def register_view(request):
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        user = form.save()
        redirect("/")
                  
    context = {
        "form": form
    } 
    return render(request, "accounts/register.html", context)


# def register_view(request):
#     if request.method == "POST":
#         firstname = request.POST["username"]
#         lastname = request.POST["lastname"]
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password1 = request.POST["password"]
#         password2 = request.POST["repeat-password"]
        
#         if password1 == password2:
#             if User.objects.filter(email=email).exists():
#                 context = {
#                     "error": "Email already exits"
#                 }
#                 return redirect("register")
            
#             elif User.objects.filter(username=username).exists():
#                 context = {
#                     "error": "Username already exits"
#                 }
#                 return redirect("register")
            
#             else:
#                 user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password1)
#                 user.save()
#                 return redirect("login")
#     else:              
#         context = {} 
#         return render(request, "accounts/register.html", context)