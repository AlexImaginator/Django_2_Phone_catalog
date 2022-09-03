from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objects = Phone.objects.all()
    sort_param = request.GET.get('sort')
    if sort_param == 'name':
        names_list = [phone_item.name for phone_item in phones_objects]
        names_list.sort()
        phones_objects = []
        for name in names_list:
            sequence_item = Phone.objects.get(name=name)
            phones_objects.append(sequence_item)
    if sort_param == 'min_price':
        prices_list = [phone_item.price for phone_item in phones_objects]
        prices_list.sort()
        phones_objects = []
        for price in prices_list:
            sequence_item = Phone.objects.get(price=price)
            phones_objects.append(sequence_item)
    if sort_param == 'max_price':
        prices_list = [phone_item.price for phone_item in phones_objects]
        prices_list.sort(reverse=True)
        phones_objects = []
        for price in prices_list:
            sequence_item = Phone.objects.get(price=price)
            phones_objects.append(sequence_item)
    context = {'phones': phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
