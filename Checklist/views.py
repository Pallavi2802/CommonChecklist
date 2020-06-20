from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib import auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from student.models import StudentProfile


# Create your views here.
class Home(APIView):
    def get(self, request):
        return render(request, 'Checklist/homepage.html') #Uncomment this to revert changes
        # return render(request, 'Checklist/addStudents.html')


class Signup(APIView):
    def get(self, request):
        return render(request, 'Checklist/signup.html')

    def post(self, request):
        if request.POST['password'] == request.POST['verifyPassword']:
            try:
                validate_email(request.POST['email'])
            except:
                return render(request, 'Checklist/signup.html', {"error": "Valid email Id please"})
            try:
                email = StudentProfile.objects.get(request.POST['email'])
                return render(request, 'Checklist/signup.html', {"error": "Account already exists"})
            except:
                pass
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'Checklist/signup.html', {'error': 'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                profile = StudentProfile(user=user, email=request.POST['email'], name=request.POST['name'],
                                         school=request.POST['school'])
                user.email = request.POST['email']
                user.save()
                profile.save()
                return render(request, 'Checklist/login.html', {"error": "Profile created. You can Login Now!"})
        else:
            return render(request, 'Checklist/signup.html', {'error': 'Passwords dont match'})


class Login(APIView):
    def get(self, request):
        return render(request, 'Checklist/login.html')

    def post(self, request):
        user = auth.authenticate(username=request.POST['Username'], password=request.POST['Password'])
        if user is not None:
            auth.login(request, user)
            try:
                is_counselor = user.counselorprofile.name
                return redirect('counselorHome')
            except:
                user.email = StudentProfile.objects.get(user=user).email
                return redirect('studentHome')
        error = "Login details error"
        return redirect('Loginuser')


class Logout(APIView):
    def get(self, request):
        auth.logout(request)
        return redirect('Loginuser')


class ChangePassword(APIView):
    def get(self, request):
        return render(request, 'Checklist/changePassword.html')

    def post(self, request):
        user = User.objects.get(username=request.user)
        if user.check_password(request.POST['current']):
            if request.POST['new'] == request.POST['newVerify']:
                user.set_password(request.POST['new'])
                user.save()
                try:
                    is_counselor = user.counselorprofile.name
                    auth.login(request, user)
                    return redirect('counselorHome')
                except:
                    auth.login(request, user)
                    return redirect('studentHome')

            else:
                return render(request, 'Checklist/changePassword.html', {"error": "Passwords don't match"})
        else:
            return render(request, 'Checklist/changePassword.html', {"error": "Current Password is not correct"})
