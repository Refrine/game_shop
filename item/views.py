from django.shortcuts import render,get_object_or_404

from .models import Item

def items(request):
    items = Item.objects.all()
    
    return render(request, 'item/items.html',{
        'items': items
    })
    
    
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item/item_detail.html', {
        'item': item
    })
