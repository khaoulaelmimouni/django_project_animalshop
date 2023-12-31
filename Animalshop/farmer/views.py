"""from django.shortcuts import render
from .models import Character
from .models import Equipement

def post_list(request):
    characters= Character.objects.all()
    equipements= Equipement.objects.all()
    return render(request,'farmer/post_list.html',{'characters':characters , 'equipements':equipements})
"""
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import farmer,sell_animal,buy

from .forms import PhotoForm
import datetime
# Create your views here.
def post_list(request):
    posts = sell_animal.objects.all()
    return render(request,'farmer/post_list.html',context={'posts':posts})

#authenctication handlers
def auth(request):
    return render(request,'farmer/auth.html')

def signin(request):
    r_email=str(request.GET['email'])
    r_passwrd=str(request.GET['password'])
    f_obj=farmer.objects.filter(email=r_email)
    if len(f_obj)==1 and f_obj[0].email==r_email and f_obj[0].password==r_passwrd:
        data='ok'
        request.session['user']=r_email
    else:
        data="notok"
    return JsonResponse({'data':data})

def signup(request):
     try:
        r_email=request.GET['email']
        r_name=request.GET['name']
        r_passwrd=request.GET['password']
        f_obj=farmer.objects.filter(email=r_email)
        if len(f_obj)==0:
            f_obj=farmer(email=r_email,name=r_name,password=r_passwrd)
            f_obj.save()
            data="ok"
        else:
         data="notok"
        return JsonResponse({'data':data})
     except KeyError:
         print(KeyError)
        
def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return redirect('/auth/')



def profile(request):
    try:
        user=request.session['user']
        print(request.session['user'])
        return render(request,'farmer/profile.html',{'obj':farmer.objects.filter(email=user)[0]})
    except:
        return redirect('/auth/')

def profileupdate(request):
    try:
        user=request.session['user']
        f_obj=farmer.objects.get(email=user)
        f_obj.name=request.GET['name']
        f_obj.street=request.GET['street']
        f_obj.city=request.GET['city']
        f_obj.district=request.GET['district']
        f_obj.phone=request.GET['phone']
        try:
            f_obj.save()
            data="ok"
        except:
            data="notok"
        return JsonResponse({'data':data})
    except:
        return redirect('/auth/')



def sell_form(request):
    try:
        user=request.session['user']
        return render(request,'farmer/sell.html')
    except:
        return redirect('/auth/')
    
"""def sell_image_view(request):
 
    if request.method == 'POST':
        form = sell_animal(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('/sell/')
    else:
        form = sell_animal()
    return render(request, 'sell.html', {'form': form})
"""



def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/sell/')
    else:
        form = PhotoForm()

    return render(request, 'upload_photo.html', {'form': form})


 
 
def success(request):
    return HttpResponse('successfully uploaded')    

def upload(request):
    try:    
        f_obj=farmer.objects.get(email=request.session['user'])
        sell_obj=sell_animal(animal_name=request.GET['name'],description=request.GET['discription'],
        f_id=f_obj,quantity=request.GET['quantity'],
        animal_race=request.GET['type'],price=request.GET['price'])
        if sell_animal.animal_race=='Les chevaux':
            sell_animal.photo='cheval'
        if sell_animal.animal_race=='Les bovins':
            sell_animal.photo='bovin'
        if sell_animal.animal_race=='Les moutons':
            sell_animal.photo='mouton'
        if sell_animal.animal_race=='Les poulets':
            sell_animal.photo='poulet'
        if sell_animal.animal_race=='Les dindes':
            sell_animal.photo='dinde'
        if sell_animal.animal_race=='Les mules':
            sell_animal.photo='mule'      
        farmer.increment_selling(f_obj)                  


        
    
        

        try:
            sell_obj.save()
            data="ok"
        except:
            data='notok'
        return JsonResponse({'data':data})
    except KeyError:
        print(KeyError)



def sale(request):
    try:
        user=request.session['user']
        x=buy.objects.values_list('p_id',flat=True)
        print(x)
        
        d=dict()
        for i in x:
            if i not in d:
                d[i]=True
            else:
                continue
        p_obj=[]
        for i in sell_animal.objects.all():
            if i.animal_id not in d:
                p_obj.append(i)
            
        return render(request,'farmer/buy.html',{'sell':p_obj})
    except :
        
        return redirect('/auth/')

def want(request):
    try:
        user=request.session['user']
        f_obj=farmer.objects.get(email=user)
        p_obj=sell_animal.objects.get(p_id=request.GET['id'])
        b_obj=buy(f_id=f_obj,p_id=p_obj,date=datetime.date.today())
        b_obj.save()
        return JsonResponse({'data':'ok'})
    except:
        return JsonResponse({'data':'notok'})