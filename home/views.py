from django.shortcuts import *
from home.models import *
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from instamojo_wrapper import Instamojo
from django.conf import settings
from django.http import JsonResponse

# Create your views here.
def home(request):
    details=Details.objects.all()
    cards=Card.objects.all()
    pizzas=Pizza.objects.all()
    context={'pizzas':pizzas,'details':details,'cards':cards}
    return render(request,'index.html',context)

def login_page(request):
    details=Details.objects.all()
    context={'details':details}
    if request.method=="POST":

        try:
            username=request.POST.get('username')
            password=request.POST.get('password')

            user_obj=User.objects.filter(username=username)
            if not user_obj.exists():
                messages.warning(request, "User not found")
                return redirect('/login/')
            
            user_obj=authenticate(username=username,password=password)
            if user_obj:
                login(request,user_obj)
                return redirect('/')
            messages.error(request, "Invalid Credentials")
            return redirect('/login/')
        
        except Exception as e:
            messages.error(request,"Something went wrong")
            return redirect('/login/')
    return render(request,'login.html',context)

def register_page(request):
    details=Details.objects.all()
    context={'details':details}
    if request.method=='POST':
        try:
            
            username=request.POST.get('username')
            password=request.POST.get('password')

            user_obj=User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username already exists")
                return redirect('/register/')
            
            user_obj=User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created Successfully!")
            return redirect('/login/')
        
        except Exception as e:
            messages.error(request,"Something went wrong")
            return redirect('/register/')
        
    return render(request,'register.html',context)

def add_cart(request,pizza_uid):
    user=request.user
    pizza_obj=Pizza.objects.get(uid=pizza_uid)
    cart,_= Cart.objects.get_or_create(user=user,is_paid=False)
    cart_items=CartItems.objects.create(
        cart=cart,
        pizza=pizza_obj
    )

    return redirect('/')

def cart(request):
    details=Details.objects.all()
    cart=Cart.objects.get(is_paid=False,user=request.user)
    context={'carts':cart,'details':details}
    return render(request,'cart.html',context)

def remove_cart_items(request,cart_item_uid):
    try:
        CartItems.objects.get(uid=cart_item_uid).delete()

        return redirect('/cart/')
    
    except Exception as e:
        print(e)

def orders(request):
    details=Details.objects.all()
    orders=Cart.objects.filter(is_paid=True,user=request.user)
    context={'orders':orders,'details':details}
    return render(request,'orders.html',context)



def logout_view(request):
    logout(request)
    return redirect('home')

def offers(request):
    details=Details.objects.all()
    offers=Offers.objects.all()
    context={'details':details,'offers':offers}
    return render(request,'offers.html',context)

def about(request):
    details=Details.objects.all()
    context={'details':details}
    return render(request,'about.html',context)

def help(request):
    details=Details.objects.all()
    context={'details':details}
    return render(request,'help.html',context)

def contact(request):
    details=Details.objects.all()
    context={'details':details}
    return render(request,'contact.html',context)


def location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        # Perform any necessary processing or API requests with the latitude and longitude
        # For simplicity, let's just return the location as a JSON response
        location = f"Latitude: {latitude}, Longitude: {longitude}"
        return JsonResponse({'location': location})
    return JsonResponse({})






