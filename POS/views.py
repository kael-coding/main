from django.shortcuts import render, redirect

# Create your views here.
products =[]
def index(request):
    return render(request ,"index.html")

def add_items(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = float(request.POST.get('price'))
        quantity = int(request.POST.get('quantity'))
        products.append({'id': len(products) + 1, 'name': name, 'price': price, 'quantity': quantity})
        return redirect('/views')
    return render(request, 'add_items.html')
    

def item_views(request):
    return render(request, 'item_views.html',  {'products': products})

