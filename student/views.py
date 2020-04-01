from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from django.contrib import auth
from .models import StudentProfile
from django.contrib.auth.forms import UserChangeForm
from .models import Essay,StudentProfile, SAT, ACT, Activity, Transcript, SubjectTest, LOR
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
class Home(APIView):
    def get(self,request):
        return render(request, 'student/studenthome.html')
class Password(APIView):
    def get(self,request):
        return render(request, 'student/changePassword.html')
    def post(self, request):
        user = User.objects.get(username = request.user)
        if user.check_password(request.POST['current']):
            if request.POST['new'] == request.POST['newVerify']:
                user.set_password(request.POST['new'])
                user.save()
                return render(request, 'student/studenthome.html')

            else:
                return render(request, 'student/changePassword.html', {"error":"Passwords don't match"})
        else:
            return render(request, 'student/changePassword.html', {"error":"Current Password is not correct"})
class ViewProfile(APIView):
    def get(self, request):
        profile = StudentProfile.objects.get(user = request.user)
        return render(request, 'student/profile.html', {"profile": profile})
    def post(self,request):
        profile = StudentProfile.objects.get(user = request.user)
        profile.email = request.POST['email']
        profile.name = request.POST['username']
        profile.school = request.POST['school']
        profile.save()
        return render(request, 'student/studenthome.html')
class Essay(APIView):
    def get(self,request):
        return render(request, 'student/essays.html')
    def post(self,request):
        if request.POST['name'] and request.POST['link'] and request.POST['date']:
            essa = Essay(user = request.user, link = request.POST['link'], name = request.POST['name'], date = request.POST['date'])
            essa.save()
            return render(request, 'student/studenthome.html')
class ViewEssay(APIView):
    def get(self, request):
        try:
            essays = Essay.objects.all()
            return render(request, 'student/viewEssays.html',{"essays":essays})
        except:
            return render(request, 'student/viewEssays.html', {"error": "You Currently have no Essays"})
class Testing(APIView):
    def get(self, request):
        sat = SAT.objects.filter(user__username = request.user);
        act = ACT.objects.all();
        subject = SubjectTest.objects.all();
        return render(request, 'student/standardised.html', {"sat":sat, "act":act, "subject":subject})
class AddSatScore(APIView):
    def get(self,request):
        try:
            scores = SAT.objects.filter(user__username = request.user)
            return render(request, 'student/standardised.html', {"tests": test})
        except:
            return render(request, 'student/standardised.html', {"error": "No Uploaded Scores"})
    def post(self,request):
        sat = SAT(user = request.user, date = request.POST['date1'], transcripts = request.FILES.get('transcript1'))
        sat.save()
        return render(request, 'student/studentHome.html', {"post": 'Score Successfully added'})
class AddActScore(APIView):
    def get(self,request):
        try:
            scores = ACT.objects.filter(user__username = request.user)
            return render(request, 'student/standardised.html', {"tests": test})
        except:
            return render(request, 'student/standardised.html', {"error": "No Uploaded Scores"})
    def post(self,request):
        act = ACT(user = request.user, date = request.POST['date2'], transcripts = request.FILES['transcript2'])
        act.save()
        return render(request, 'student/studentHome.html', {"post": 'Score Successfully added'})
class AddSubjectScore(APIView):
    def get(self,request):
        try:
            scores = SAT.objects.all().filter(user__username = request.user)
            return render(request, 'student/standardised.html', {"tests": test})
        except:
            return render(request, 'student/standardised.html', {"error": "No Uploaded Scores"})
    def post(self,request):
        subject = SubjectTest(user = request.user, date = request.POST['date3'], transcripts = request.FILES['transcript3'])
        subject.save()
        return render(request, 'student/studentHome.html', {"post": 'Score Successfully added'})

class Activity(APIView):
    def get(self, request):
        try:
            activity = Activity.objects.filter(user__username = request.user)
            return render(request, 'student/activity.html', {"activity":activity})
        except:
            return render(request, 'student/activity.html', {"error":"No activities yet"})
    def post(self,request):
        activity = Activity(user = request.user, name = request.POST['name'],category = request.POST['category'], grades = request.POST['grades'], position =request.POST['position'], hourperweek = request.POST['hoursperweek'], weeksperyear =request.POST['weeksperyear'], awards = request.POST['awards'], description = request.POST['description'])
        activity.save()
        return render(request, 'student/studenthome.html')
class Transcript(APIView):
    def get(self,request):
        try:
            transcript = Transcript.objects.filter(user__username = request.user)
            return render(request, 'student/transcript.html', {"transcript": transcript})
        except:
            return render(request, 'student/transcript.html', {"error":"No transcripts uploaded yet"})
    def post(self,request):
        transcript = Transcript(user = request.user, grade = request.POST['grade'], transcript = request.FILES['transcript'])
        transcript.save()
        return render(request, 'student/studenthome.html')
class LOR(APIView):
    def get(self,request):
        try:
            lor = LOR.objects.filter(user__username = request.user)
            return render(request, 'student/lor.html', {"lor": LOR})
        except:
            return render(request, 'student/lor.html', {"error":"No transcripts uploaded yet"})
    def post(self,request):
        lor = LOR(user = request.user, recommender = request.POST['recommender'], lor = request.FILES['transcript'])
        lor.save()
        return render(request, 'student/studenthome.html')