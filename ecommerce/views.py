from django.shortcuts import *
from . models import *
from . forms import *
# Create your views here.
def InsertEdit(request,pk=None):
    instance=get_object_or_404(Product,id=pk) if pk else None
    if request.method=="POST":
        form=ProductForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("allproduct")
    else:
            form=ProductForm(instance=instance)
            return render(request,"InsertEdit.html",{'form':form})
def Delete(request,pk):
    product=get_object_or_404(Product,id=pk)
    if request.method=="POST":
        product.delete()
        return redirect("alproduct")
    else:
        return render(request,"DeleteConfirm.html",{'product':product})
    
def Addcategory(request,pk=None):
    instance=get_object_or_404(Category,id=pk) if pk else None
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("allcategory")
    else:
        form=CategoryForm(instance=instance)
        return render(request,"addcategory.html",{'form':form})
def AllProduct(request):
    product=Product.objects.all()
    return render(request,"allproduct.html",{'product':product})
def DeleteCategory(request,pk):
    category=get_object_or_404(Category,id=pk)
    category.delete()
    return redirect("allcategory")
def AllCategory(request):
    category=Category.objects.all()
    return render(request,"allcategory.html",{'category':category})