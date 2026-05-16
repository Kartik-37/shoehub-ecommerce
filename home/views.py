from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.db.models import Max,Sum,Count
from .models import Contact,Items,Type,Category,Cart,Account,Billing,Payment
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect


def index(request):
    data = Items.objects.filter(type=1)
    best = Items.objects.filter(category=3)
    context={
        "data":data,
        "best":best,
    }
    return render (request,'../templates/index.html',context)

def about(request):
    return render (request,'../templates/about.html')

def gymsneakers(request):
    data = Items.objects.filter(type=1)
    context={"data":data,}
    return render (request,'../templates/gym sneakers.html',context)

def hikesneakers(request):
    data = Items.objects.filter(type=2)
    context={"data":data,}
    return render (request,'../templates/hike sneakers.html',context)

def worksneakers(request):
    data = Items.objects.filter(type=3)
    context={"data":data,}
    return render (request,'../templates/work sneakers.html',context)

def chucksneakers(request):
    data = Items.objects.filter(type=4)
    context={"data":data,}
    return render (request,'../templates/chuck sneakers.html',context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        sql = Contact(name=name,email=email,phone=phone,message=message)
        sql.save()
        return render (request,'../templates/index.html')

    return render (request,'../templates/contact.html')

def man(request):

    data = Items.objects.filter(category=1)
    context={"data":data,}
    return render (request,'../templates/man.html',context)

def women(request):
    data = Items.objects.filter(category=2)
    context={"data":data,}
    return render (request,'../templates/women.html',context)

def kid(request):
    data = Items.objects.filter(category=3)
    context={"data":data,}
    return render (request,'../templates/kid.html',context)

def register(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        obj = Account(
            username=name,
            email=email
        )
        obj.save()

        # Automatically login user
        login(request, user)

        return redirect('home')

    return render(request, '../templates/logregis.html')
# def register(request):
#     if request.method == "POST":
#         name = request.POST.get("name") 
#         email = request.POST.get("email") 
#         password = request.POST.get("password") 
#         sql = User.objects.create_user(username=name,email=email,password=password)
#         sql.save()
#         obj = Account(username=name,email=email)
#         obj.save()
#         return redirect ('home')

#     return render (request,'../templates/logregis.html')

def login_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]

    user = authenticate(request,username=name, password=password)

    if user is not None:
             login(request,user)
             return redirect ('home')
    else:
             return render (request,'../templates/logregis.html')
    
    return render (request,'../templates/logregis.html')

def logout_view(request):
    logout(request)
    return redirect('home') 

def detail(request,id):
    data = Items.objects.filter(pk=id)
    loop = Items.objects.filter(type=4)
    context={
        "data":data,
        "loop":loop,
    }
    return render (request,'../templates/detail.html',context)

def cart(request):
    
    if request.user.is_authenticated:
            user1 = request.user
    data1=Cart.objects.filter(username=user1)
    data = Cart.objects.filter(username=user1)
    total=0
    total1=0
    for i in data1:
        total=total+i.price
    total1=total+100
    context={
        "data1":data1,
        "total":total,
        "total1":total1,
        "data":data,
    }

    return render (request,'../templates/cart.html',context)

def cart1(request,id):

    if request.user.is_authenticated:
            user1 = request.user

            data = Items.objects.filter(pk=id)
            for i in data:
                name = i.name
                price = i.price
                image = i.image1
                size1 = i.size1
                size2 = i.size2
                size3 = i.size3
                size4 = i.size4
                size5 = i.size5
                width1 = i.width1
                width2 = i.width2
                width3 = i.width3
                width4 = i.width4
                obj=Cart(pid=id,username=user1,name=name,price=price,image=image,size1=size1,size2=size2,size3=size3,size4=size4,size5=size5,width1=width1,width2=width2,width3=width3,width4=width4)
                obj.save()
                return redirect ('cart')
    else:
         return redirect('register')
   
def delcart(request,id):

    if request.user.is_authenticated:
            user1 = request.user
    
    data=Cart.objects.filter(pk=id)
    data.delete()
    return redirect ('cart')

def account(request):
    if request.user.is_authenticated:
            username = request.user

    data1=Billing.objects.filter(username=username)
    data = Account.objects.filter(username=username)
    context={
            'data1':data1,
            'data':data,
            'username':username,
        }
    return render (request,'../templates/account.html',context)

def edit(request):
    if request.user.is_authenticated:
            username = str(request.user)
    
    data = Account.objects.filter(username=username).first()
    if request.method == "POST":
            name= request.POST.get("name")
            email= request.POST.get("email")
            phone= request.POST.get("phone")
            address= request.POST.get("address")
            city= request.POST.get("city")
            state= request.POST.get("state")
            pincode= request.POST.get("pincode")
            if data is None:
                    sql = Account(username=username,name=name,email=email,phone=phone,address=address,city=city,state=state,pincode=pincode)
                    sql.save()
            else:
                    sql = Account.objects.filter(username=username).update(name=name,email=email,phone=phone,address=address,city=city,state=state,pincode=pincode)

    return redirect('account')

def invoice(request):
        return render (request,'../templates/payment.html')

def payment(request):
    if request.user.is_authenticated:
            username = request.user

   
    last_order = Payment.objects.aggregate(Max('oid'))['oid__max']
    if last_order is None:
        id = 1
    else:
        id = last_order+1
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        phone = request.POST.get("phone")
        cname = request.POST.get("cname")
        expdate = request.POST.get("expdate")
        cvv = request.POST.get("cvv")
        cardno = request.POST.get("cardno")
        sql = Payment(oid=id,username=username,fname=fname,lname=lname,address=address,city=city,state=state,pincode=pincode,phone=phone,cname=cname,expdate=expdate,cvv=cvv,cardno=cardno)
        sql.save()
        

    data = Cart.objects.filter(username=username)
    data1 = Payment.objects.filter(oid=id)
    for i in data:
         cid = i.cid
         pid = i.pid
         name = i.name
         image = i.image
         price = i.price
         obj=Billing(oid=id,cid=cid,username=username,pid=pid,name=name,image=image,price=price)
         obj.save()
    data2= Billing.objects.filter(oid=id)
    total=0
    total1=0
    for i in data2:
                total=total+i.price
    total1=total+100

    context = {
                "data2":data2,
                "data1":data1,
                "total":total,
                "total1":total1,
            }
    data=Cart.objects.all()
    data.delete()

    return render (request,'../templates/invoice.html',context)

    return render (request,'../templates/payment.html')

def admindesk(request):
    data=Billing.objects.aggregate(Sum('price'))['price__sum']
    data1=Items.objects.aggregate(Count('name'))['name__count']
    data2=Billing.objects.aggregate(Count('oid'))['oid__count']
    data3=Account.objects.aggregate(Count('username'))['username__count']
    data4=Billing.objects.order_by('-oid')
    context={
         'data':data,
         'data1':data1,
         'data2':data2,
         'data3':data3,
         'data4':data4,
    }
    return render (request,'../templates/admindesk.html',context)
def adminuser(request):
    data=Account.objects.all()
    context={
         'data':data,
    }
    return render (request,'../templates/auser.html',context)
def adminorder(request):
    data=Billing.objects.all()
    context={
         'data':data,
    }
    return render (request,'../templates/aorder.html',context)
def adminproduct(request):
    data=Items.objects.all()
    context={
         'data':data,
    }
    return render (request,'../templates/aproduct.html',context)



# Create your views here.
