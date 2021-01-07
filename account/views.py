from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contact, Blog, Designs3D, Image, Vastu

# Create your views here.
def index(request):
    categories = Designs3D.objects.all()
    blogs = Blog.objects.all().order_by('id')
    context = {
        'categories': categories,
        'blogs': blogs
    }
    return render(request, 'index.html', context)

def single(request):
    cat = Designs3D.objects.get(category_name='Interior Designing')
    cat2 = Designs3D.objects.get(category_name='Flat Decors')
    interior = Image.objects.filter(category=cat.id)
    flat =Image.objects.filter(category=cat2.id)
    specials = Vastu.objects.all()
    context = {
        'flat': flat,
        'hallDecor': cat,
        'flatDecor': cat2,
        'interior':interior,
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
        contactData = Contact(first_name=first_name, last_name=last_name, email=email, contact=contact, notes=notes)
        contactData.save()
        return redirect('index')
    except:
        return render(request, 'index.html', {"msg": "Every Field Is Required !!!"})
