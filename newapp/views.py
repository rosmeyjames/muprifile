from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import portfolioform, projectform, profileform
from.models import profile,project,portfolio
def search(request):
    query=None
    p=None
    if 'q' in request.GET:
        query = request.GET.get('q')

        p = profile.objects.filter(Q(name__icontains=query))

        # p=profile.objects.filter(Q(name__icontains=querry))
    else:
        p=[]
        return redirect('register')
    context={'p':p,'query':query}
    return render(request,'search.html',context)
def register(request):
    if request.method=='POST':
       # first_name,last_name
       username= request.POST.get('username')
       email= request.POST.get('email')
       password=request.POST.get('password')
       confirmpassword=request.POST.get('confirmpassword')
       if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
            return redirect('login')
       else:
            messages.info(request, 'password mismatch')
            return redirect(register)
    return render(request,'register.html',)
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/createprofile')
            # return render(request, 'login.html')
        else:
            messages.info(request,'provide correct details')
            return redirect('login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('login')
def home(request):
    return render(request,'home.html')
# def search(request,q):
#
#
#     try:
#         # Retrieve the user profile with ID 1
#         first_profile = profile.objects.get(name=q)
#         # Now you can access attributes of the retrieved profile, e.g., first_profile.name
#     except profile.DoesNotExist:
#         # Handle the case where the record doesn't exist
#         pass
#         render(request, 'search.html', {'first_profile':first_profile})

# def index(request):
#     return render(request,'index.html')

# Create your views here.
def listproject(request):
    projects = project.objects.all()
    paginator = Paginator(projects, 2)
    page_number = request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request, 'listproject.html', {'page': page})
def listportfolio(request):
    portfolios = portfolio.objects.all()
    paginator = Paginator(portfolios, 2)
    page_number = request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request, 'listportfolio.html', {'page': page})
def listprofile(request):
    profiles = profile.objects.all()
    paginator = Paginator(profiles, 2)
    page_number = request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request, 'listprofile.html', {'page': page})
def createprofile(request):
    profiles = profile.objects.all()
    paginator = Paginator(profiles, 2)
    page_number = request.GET.get('page')
    # Corrected attribute name
    if request.method == 'POST':
        form = profileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = profileform()

    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    # return render(request, 'profile.html', {'form':form,'profiles': profiles})
    return render(request, 'profile.html', {'form': form, 'page':page})

def updateprofile(request,profileid):
    profiles = profile.objects.get(id=profileid) # Corrected attribute name
    if request.method == 'POST':
        form = profileform(request.POST,request.FILES,instance=profiles)
        if form.is_valid():
            form.save()
            return redirect('createprofile')
    else:
        form = profileform(instance=profiles)
    return render(request, 'update.html', {'form':form})
def updateportfolio(request,portfolioid):
    portfolios = portfolio.objects.get(id=portfolioid) # Corrected attribute name
    if request.method == 'POST':
        form = portfolioform(request.POST,request.FILES,instance=portfolios)
        if form.is_valid():
            form.save()
            return redirect('createportfolio')
    else:
        form = portfolioform(instance=portfolios)
    return render(request, 'update.html', {'form':form})
def detailsprofile(request,profileid):
    det=profile.objects.get(id=profileid)
    return render(request,'profiledetail.html',{'det':det})
def detailsportfolio(request,portfolioid):
    det=portfolio.objects.get(id=portfolioid)
    return render(request,'portfoliodetail.html',{'det':det})
def detailsproject(request,projectid):
    det=project.objects.get(id=projectid)
    return render(request,'projectdetail.html',{'det':det})
def deleteportfolio(request,portfolioid):
    d = portfolio.objects.get(id=portfolioid)
    if request.method == 'POST':
        d.delete()
        return redirect('/')
    return render(request, 'delete.html', {'d': d})
def deleteproject(request,projectid):
    d = project.objects.get(id=projectid)
    if request.method == 'POST':
        d.delete()
        return redirect('/')
    return render(request, 'delete.html', {'d': d})
def deleteprofile(request,profileid):

    d=profile.objects.get(id=profileid)
    if request.method == 'POST':
        d.delete()
        return redirect('/')
    return render(request,'delete.html',{'d':d})

def updateproject(request,projectid):
    projects = project.objects.get(id=projectid) # Corrected attribute name
    if request.method == 'POST':
        form = projectform(request.POST,files=request.FILES,instance=projects)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = projectform(instance=projects)
    return render(request, 'update.html', {'form':form})
def createportfolio(request):
    portfolios = portfolio.objects.all()

    paginator = Paginator(portfolios, 2)
    page_number = request.GET.get('page')
    if request.method=='POST':
        form=portfolioform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=portfolioform()
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request,'portfolio.html',{'form':form,'page':page})
# def createproject(request):
#     books=Book.object.all()
#
#     if request.method=='POST':
#         tiitle=request.post.get()
#         price =request.post.get()
#         book=Book('title'=title,'price'=price)
#         book.save()
#         return render(request,'book.html',{'books':books})
def createproject(request):
    projects = project.objects.all()
    paginator = Paginator(projects, 2)
    page_number = request.GET.get('page')
    if request.method=='POST':
        form=projectform(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=projectform()
    try:
        page = paginator.get_page(page_number)
    except EmptyPage:
        page = paginator.page(page_number.num_pages)
    return render(request, 'project.html', {'page': page,'form':form})

