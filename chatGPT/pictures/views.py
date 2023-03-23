from pictures.forms import PictureForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from pictures.models import Pictures
from pictures.gpt import GPT_function, creating_picture
from django.contrib import messages


def picture_view(request):
    template = 'pictures/index.html'
    title = 'AI Generated'
    form = PictureForm()
    context = {
        'form': PictureForm,
        'title': title
    }
    if request.method != 'POST':
        return render(request, template, context)
    
    form = PictureForm(request.POST)

    if form.is_valid():
        name = form.data['name']
        my_picture = form.save()

        my_picture = get_object_or_404(Pictures, id=my_picture.id)

        gpt_return = GPT_function(name)

        if 'http' not in str(gpt_return):
            my_picture.delete()
            messages.warning(request, gpt_return)
            return redirect('pictures:index')
        
        my_picture.picture_url = gpt_return
        creating_picture(my_picture)
        my_picture.save()
        return redirect('pictures:list')
    return render(request, template, context)


def picture_view_list(request):
    objects = Pictures.objects.all()
    context = {
        'objects': objects
    }
    template = 'pictures/list.html'
    return render(request, template, context)


def picture_detail(request, id):
    obj = get_object_or_404(Pictures, id=id)
    context = {
        'object': obj
    }
    template = 'pictures/detail.html'
    return render(request, template, context)


def picture_clear(request):
    pics = Pictures.objects.filter(Q(picture_url='') | Q(picture=''))
    pics.delete()
    return redirect('pictures:list')
