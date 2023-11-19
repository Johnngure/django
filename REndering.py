from django.shortcuts import render
 
def myview(request):  

      if request.method=='GET':  
            #perform read or delete operation on the model  

      if request.method=='POST':  
            #perform insert or update operation on the model  
            context={ } #dict containing data to be sent to the client  

      return render(request, 'mytemplate.html', context) 