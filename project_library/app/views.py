from django.shortcuts import render,redirect
import requests
from django.conf import settings
from django.contrib import messages
import json

url = settings.URL 

# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name =  request.POST['txtUserName']
        password =  request.POST['txtPassword']
        data={
            'username':user_name,
            'password':password,
        }
        response = requests.post('{url}login/'.format(url=url) ,data=data) 
        print(response.text)
        if response.status_code==200:
            messages.success(request,('Logged in successful'))
            print(response.text)
            dict=json.loads(response.text) 
            Token=(dict["access"])
            user_role=(dict["role"])
            print(Token)
            print(user_role)
            # for getting session variable:
            request.session['get_access'] = Token 
            request.session['get_username'] = user_name 
            request.session['get_role'] = user_role
            print('-----------------------div------------------')
            print(user_name)
            print(user_role)
            print(type(user_role))
            print(type(dict))
            print(Token)

            # for setting session variable:
            # get_token = request.session.get('get_token')

            if user_role == "LIBRARIAN":
                print('---------------------its librarian---------------------')
                return redirect('library_management') 
            else:
                print('---------------------its member---------------------')
                return redirect('member_management')
        else:
            messages.error(request,("Wrong credentials. Try Again"))
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        user_name =  request.POST['txtUserName']
        password1 = request.POST['txtPassword1']
        password2 = request.POST['txtPassword2']
        if password1 == password2:
            data = {
                'username' : user_name,
                'password' : password1
                }
            # validation for username already exists in serializer
            response = requests.post('{url}create_user/'.format(url=url) ,data=data)
            print('-------------register-------------') 
            print(response.text)
            return redirect('login')
    else:
        return render(request,'register.html')


def library_management(request):
    if request.POST.get('btnSavebook','') == 'SaveBook':
        print('------------post book-------------')
        name=request.POST['txtBookName']
        author=request.POST['txtAuthor']
        book_number=request.POST['txtBookNumber']
        category=request.POST['txtCategory']

        data={
            'name':name,
            'author':author,
            'book_number':book_number,
            'category':category,
            }
        response=requests.post('{url}create_book/'.format(url=url), data=data)
        print('------------postdata-------------')     
        messages.success(request,("Book added successfully"))
        return redirect('list_books_and_members')
    if request.POST.get('btnSaveMember','') == 'SaveMember':
        print('------------post member-------------')
        user=request.POST['txtMemberName']
        role=request.POST['txtMemberRole']
        data={
            'user':user,
            'role':role,
            }
        response=requests.post('{url}create_book/'.format(url=url), data=data)
        print('------------postdata-------------')     
        messages.success(request,("Member added successfully"))
        return redirect('list_books_and_members')
    else:
        print('-------------------------else-------------')
        role_data=requests.get('{url}create_user/'.format(url=url)).json() 
        return render(request,'library/library_management.html',{'role_data':role_data})

def member_management(request):
    return render(request,'member/member_management.html')

def list_books_and_members(request):
    book_data=requests.get('{url}create_book/'.format(url=url)).json()
    user_data=requests.get('{url}create_user/'.format(url=url)).json()
    return render(request,"library/list_books_and_members.html",{'book_data':book_data,'user_data':user_data})
