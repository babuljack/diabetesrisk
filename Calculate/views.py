from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
# Create your views here.
class Index(View):
    def get(self,request):
        return render(request,'index.html')

class DiabetesCalculate(View):
    def get(self,request):
        age=int(request.GET.get('age'));
        gender=int(request.GET.get('gender'));
        aboriginal=int(request.GET.get('aboriginal'));
        born=int(request.GET.get('born'));
        diagnosed=int(request.GET.get('diagnosed'));
        hbg=int(request.GET.get('hbg'));
        hbp=int(request.GET.get('hbp'));
        smoke=int(request.GET.get('smoke'));
        fruitVeg=int(request.GET.get('fruitVeg'));
        activity=int(request.GET.get('activity'));
        waist=int(request.GET.get('waist'));
        wasitpoint=0
        #asian 
        if born == 2:
            #Asia man calcullate
            if waist < 90 and gender == 3:
                wasitpoint=0
            if waist >= 90 and waist <= 100 and gender == 3:
                wasitpoint=4
            if waist > 100 and gender == 3:
                wasitpoint=7  

            #Asia woman calcullate
            if waist < 80 and gender == 0:
                wasitpoint=0
            if waist >= 80 and waist <= 90 and gender == 0:
                wasitpoint=4
            if waist > 90 and gender == 0:
                wasitpoint=7          
        #Not asian 
        if born == 0:
            #Not Asia man calcullate
            if waist < 102 and gender == 3:
                wasitpoint=0
            if waist >= 102 and waist <= 110 and gender == 3:
                wasitpoint=4
            if waist > 110 and gender == 3:
                wasitpoint=7  

            #Not Asia woman calcullate
            if waist < 88 and gender == 0:
                wasitpoint=0
            if waist >= 88 and waist <= 100 and gender == 0:
                wasitpoint=4
            if waist > 100 and gender == 0:
                wasitpoint=7    
        score=age+gender+aboriginal+born+diagnosed+hbg+hbp+smoke+fruitVeg+activity+wasitpoint
        return JsonResponse({'data':score})

