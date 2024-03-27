from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate,logout,login
# Create your views here.
@api_view(['GET','POST'])
def Index(request):
    if  request.method == 'GET':
        return Response({'message':'Hello World!'})
    if request.method=='POST':
        data=request.data
        print(data)
        user = data['userid']
        pwd = data['password']
        # print(username,password)
        validuser=authenticate(request,username=user,password=pwd)
        if validuser != None:
            login(request,validuser)
            print(request.user.username)
            return Response({"success":True,"msg":"Successfully Post!"},status=201)
        else:
            print("not a vlaid user")
            return Response({"success":False,"msg":"not a valid dat"})   
@api_view(['POST'])         
def logoutuser(request):
    print("--------------",request.user.username)
    logout(request)
    print("--------------",request.user.username)
    return Response({"success":True,"msg":"Logged out Successfully"},status=200)  
    
        