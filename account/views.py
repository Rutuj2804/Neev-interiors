from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contact, Blog, Categorie, Image, Special

# Create your views here.
def index(request):
    categories = Categorie.objects.all()
    blogs = Blog.objects.all().order_by('id')
    context = {
        'categories': categories,
        'blogs': blogs
    }
    return render(request, 'index.html', context)

def single(request):
    cat = Categorie.objects.get(category_name='Hall Decor')
    cat2 = Categorie.objects.get(category_name='Flat Decors')
    cat3 = Categorie.objects.get(category_name='Bedroom Decor')
    cat4 = Categorie.objects.get(category_name='Room Decor')
    cat5 = Categorie.objects.get(category_name='Kitchen Decor')
    hall = Image.objects.filter(category=cat.id)
    bed = Image.objects.filter(category=cat3.id)
    flat =Image.objects.filter(category=cat2.id)
    room =Image.objects.filter(category=cat4.id)
    kitchen =Image.objects.filter(category=cat5.id)
    specials = Special.objects.all()
    context = {
        'hall': hall,
        'flat': flat,
        'bed': bed,
        'room': room,
        'kitchen': kitchen,
        'hallDecor': cat,
        'flatDecor': cat2,
        'bedDecor': cat3,
        'roomDecor': cat4,
        'kitchenDecor': cat5,
        'specials': specials
    }
    return render(request, 'single.html',  context)

def blogs(request):
    blogposts = Blog.objects.all().order_by('-created_at')
    context = {
        'blogs': blogposts
    }
    return render(request, 'blog-layout.html', context)

def contact(request):
    try:
        first_name = request.POST['Firstname']
        last_name = request.POST['Lastname']
        email = request.POST['Email']
        contact = request.POST['Contact']
        notes = request.POST['notes']
        if(first_name>0 & last_name>0 & email>0 & contact>0 & notes>0 ):
            contactData = Contact(first_name=first_name, last_name=last_name, email=email, contact=contact, notes=notes)
            contactData.save()
            return redirect('index')
    except:
        return render(request, 'index.html', {"msg": "Every Field Is Required !!!"})
    return render(request, 'single.html')