from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse




def index(request):
    recommends = Restaurant.objects.all()
    context ={
        'recommends' : recommends,
    }
    return render(request, "recommends/index.html", context)


def seoul_main(request):
    recommends = Restaurant.objects.filter(region = 1)
    images = Images.objects.all()
    context ={
        'recommends' : recommends,
        'images' : images,
    }
    return render(request, "recommends/seoul_main.html", context)



def busan_main(request):
    recommends = Restaurant.objects.filter(region = 2)
    context ={
        'recommends' : recommends,
    }
    return render(request, "recommends/busan_main.html", context)


def etc_main(request):
    recommends = Restaurant.objects.filter(region = 3)
    context ={
        'recommends' : recommends,
    }
    return render(request, "recommends/etc_main.html", context)



def comments_create(request, restaurant_pk ):
    recommend = Restaurant.objects.get(pk=restaurant_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit = False)
        comment.restaurant = recommend
        comment.save()    
    if recommend.region == '1' :
        return redirect('buk2on_on:seoul_main' )
    elif recommend.region == '2' :
        return redirect('buk2on_on:busan_main' )
    elif recommend.region == '3' :
        return redirect('buk2on_on:etc_main' )


def detail(request, restaurant_pk ):
    recommend = Restaurant.objects.get(pk=restaurant_pk)
    comment_form = CommentForm()
    comments = recommend.comments.all()
    context = {
        'recommend' : recommend,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'recommends/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=4)
    
    if request.method == "POST" :
        restaurantform = RestaurantForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES)
        if restaurantform.is_valid() and formset.is_valid():
            restaurant_form = restaurantform.save(commit=False)
            restaurant_form.user = request.user
            restaurant_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(restaurant=restaurant_form, image=image)
                    photo.save()

            if request.POST['region'] == '1' :
                return redirect('buk2on_on:seoul_main' )
            elif request.POST['region'] == '2' :
                return redirect('buk2on_on:busan_main' )
            elif request.POST['region'] == '3' :
                return redirect('buk2on_on:etc_main' )

    else:
        Recommendform = RestaurantForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        context = {
            'Recommendform' : Recommendform,
            'formset' : formset,
        }
    return render(request, 'recommends/create.html', context)


@require_POST
def delete(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    restaurant_region = restaurant.region
    restaurant.delete()
    if restaurant_region == '1':
        return redirect('buk2on_on:seoul_main' )
    if restaurant_region == '2':
            return redirect('buk2on_on:busan_main' )
    if restaurant_region == '3':
            return redirect('buk2on_on:etc_main' )


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, restaurant_pk):
    ImageFormSet = modelformset_factory(Images,form=ImageForm, extra=4)

    restaurant = Restaurant.objects.get(pk=restaurant_pk)

    if request.method == 'POST':
        restaurant_form = RestaurantForm(request.POST, request.FILES, instance=restaurant)
        formset = ImageFormSet(request.POST, request.FILES)
        if restaurant_form.is_valid() and formset.is_valid() :
            restaurant_form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(restaurant=restaurant_form, image=image)
                    photo.save()
                
            return redirect('buk2on_on:detail', restaurant.pk)
                

        else:
            print(restaurant_form.errors, formset.errors)

    else:
        restaurant_form = RestaurantForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    context = {
            'restaurant_form' : restaurant_form,
            'formset' : formset,
        }
    return render(request, 'recommends/update.html', context)