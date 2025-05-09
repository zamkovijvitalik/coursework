from django.shortcuts import render

def index(request):
    return render(request, 'my.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def order(request):
    if request.method == 'POST':
        selected_items = [item for item in menu_items if request.POST.get(item['name'])]
        return render(request, 'order_success.html', {'selected_items': selected_items})
    return render(request, 'order.html', {'menu_items': menu_items})