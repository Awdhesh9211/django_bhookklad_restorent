from django.shortcuts import render
from django.http import HttpResponse
from base.models import BookTable, AboutUs, Feedback, ItemList, Items
# Create your views here.

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    for k in review:
            print(k.Image.url)
    
    return render(request, 'home.html',{'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request,category):
    # items =  Items.objects.all()
    # print(category)
    # category=ItemList.objects.filter(Category_name=category)
    # for i in category:
    #     print()
    # if category == 'all':
    #    items =  Items.objects.all()
    # else:
    #    items=Items.objects.filter(Category=category.id)
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


# def MenuViewByCategory(request):
#     list=get_object_or_404(ChaiVarity , pk=category)
#     return render(request, 'menu.html', {'items': items, 'list': list})



def BookTableView(request):
    if request.method=='POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')

        if name != '' and len(phone_number) == 10 and email != '' and total_person != 0 and booking_data != '':
            data = BookTable(Name=name, Phone_number=phone_number,
                             Email=email,Total_person=total_person,
                             Booking_date=booking_data)
            data.save()
    return render(request, 'book_table.html')



def FeedbackView(request):
    if request.method=='POST':
        username = request.POST.get('user_name')
        desc = request.POST.get('Description')
        rating = request.POST.get('rating')
        profile = request.POST.get('file')
        if username != '' and len(rating) >= 1 and desc != '':
            data = Feedback(User_name = username,Description =desc,Rating = rating,Image = profile)
            data.save()
    return render(request, 'feedback.html')