from django.shortcuts import render
from .models import Product
from .models import Location
from .models import Inventory
from .models import ProductMovement
from django.http import HttpResponse

def formProduct(request):
    return render(request,'addProduct.html')

def addProduct(request):
    if request.method == 'POST':
        if request.POST.get('Prod_ID') and request.POST.get('Prod_Name') and request.POST.get('qty'):
            Prod=Product()
            Prod.P_id= request.POST.get('Prod_ID')
            Prod.P_name= request.POST.get('Prod_Name')
            Prod.qty= request.POST.get('qty')
            Prod.save()

            Inv=Inventory()
            Inv.Prod= Prod.P_name
            Inv.Prod_id = Prod.P_id
            Inv.Loc_name= "new"
            Inv.Quantity= Prod.qty
            Inv.save()

            return render(request, 'addProduct.html')  
        else:
            return render(request,'addProduct.html')

def viewProduct(request):
    prod=Product.objects.all() # Collect all records from table 
    return render(request, 'productView.html',{"prod":prod})

def formLocation(request):
    return render(request,'addLocation.html')

def addLocation(request):
    if request.method == 'POST':
        if request.POST.get('Loc_ID') and request.POST.get('Loc_Name'):
            Loc=Location()
            Loc.Loc_id= request.POST.get('Loc_ID')
            Loc.Loc_name= request.POST.get('Loc_Name')
            Loc.save()
            return render(request, 'addLocation.html')  
        else:
            return render(request,'addLocation.html')

def viewLocation(request):
    Loc=Location.objects.all() # Collect all records from table 
    return render(request, 'LocationView.html',{"Loc":Loc})

def viewInventory(request):
    Inv=Inventory.objects.all()

    return render(request, "index.html",{"Inv": Inv})

def formProductMove(request,P):
    queryset = Inventory.objects.filter(id=P).values("id","Prod","Prod_id","Loc_name", "Quantity")
    que = queryset[0]
    
    Loc = Location.objects.all()
    return render(request,'MoveProduct.html', {'que' : que, 'Loc':Loc})

def Movement(request):
    if request.method == 'POST':
        Mov = ProductMovement()
        Mov.Movement_id = request.POST.get('M_ID')
        Mov.Prod_id = request.POST.get('P_ID')
        Mov.Loc_From = request.POST.get('Loc_From')
        Mov.Loc_To = request.POST.get('SelectedLoc')
        Mov.timestamp = request.POST.get('timestamp')
        Mov.Quantity= request.POST.get('qty')
        Mov.save()

        Inv=Inventory()
        Inv.Prod= request.POST.get('P_Name')
        Inv.Prod_id = request.POST.get('P_ID')
        Inv.Loc_name= request.POST.get('SelectedLoc')
        Inv.Quantity= request.POST.get('qty')
        Inv.save()
            
        qty = request.POST.get('qty')
        ID = request.POST.get('Id')
        Inventory_edit = Inventory.objects.get(id=ID) # object to update
        Inventory_edit.Quantity =  int(Inventory_edit.Quantity)-int(qty) # update name
        if Inventory_edit.Quantity <= 0:
            Inventory_edit.delete()
        else:
            Inventory_edit.save() # save object 
        
    return render(request,'success.html')

def viewHistoty(request):
    Mov=ProductMovement.objects.all()
    return render(request, "movementHistory.html",{"mov": Mov})