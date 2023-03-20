from pictures.forms import PictureForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from pictures.models import Pictures
from pictures.gpt import GPT_function, creating_picture


def picture_view(request):
    template = 'pictures/index.html'
    title = 'AI Generated'

    if request.method != 'POST':
        form = PictureForm()
        context = {
            'form': PictureForm,
            'title': title
        }
        return render(request, template, context)
    
    form = PictureForm(request.POST)
    init_name = form.data['name']
    form.data._mutable = True
    form.data['name'] = init_name.strip(' ')
    form.data._mutable = False

    if form.is_valid():
        name = form.data['name']
        form.save()

        my_picture = Pictures.objects.filter(name__exact=name)[0]

        gpt_return = GPT_function(name)

        if gpt_return == 'http://unavailable':
            my_picture.delete()
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
