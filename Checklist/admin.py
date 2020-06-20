from django.contrib import admin
# from student.models import Essay,StudentProfile, SAT, ACT, Activity,Invite, Transcript, SubjectTest, LOR
from student.models import Essay, StudentProfile, Activity, Invite, Transcript, LOR, Testing, Notes, Deadline
from Counselor.models import CounselorProfile, Link
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.

class StudentProfileInline(admin.TabularInline):
    model = StudentProfile
    can_delete = False
    verbose_name_plural = 'StudentProfiles'


class CounselorProfileInline(admin.TabularInline):
    model = CounselorProfile
    can_delete = False
    verbose_name_plural = 'Counselor Profiles'


class EssaysInline(admin.TabularInline):
    model = Essay
    can_delete = False
    verbose_name_plural = 'Essays'


class NotesInline(admin.TabularInline):
    model = Notes
    can_delete = False
    verbose_name_plural = 'Notes'


class DeadlineInLine(admin.TabularInline):
    model = Deadline
    can_delete = False
    verbose_name_plural = 'Deadlines'


class LinkInLine(admin.TabularInline):
    model = Link
    can_delete = False
    verbose_name_plural = 'Links'


# class SATInline(admin.TabularInline):
#     model = SAT
#     can_delete = False
#     verbose_name_plural = 'SATs'
#
# class ACTInline(admin.TabularInline):
#     model = ACT
#     can_delete = False
#     verbose_name_plural = 'ACTs'
#
# class SubjectTestInline(admin.TabularInline):
#     model = SubjectTest
#     can_delete = False
#     verbose_name_plural = 'SubjectTests'

class TestingInLine(admin.TabularInline):
    model = Testing
    can_delete = False
    verbose_name_plural = 'tests'


class ActivityInline(admin.TabularInline):
    model = Activity
    can_delete = False
    verbose_name_plural = 'Activities'


class TranscriptInline(admin.TabularInline):
    model = Transcript
    can_delete = False
    verbose_name_plural = 'Transcripts'


class LORInline(admin.TabularInline):
    model = LOR
    can_delete = False
    verbose_name_plural = 'LORs'


class InviteInline(admin.TabularInline):
    model = Invite
    can_delete = False
    verbose_name_plural = 'Invites'


class UserAdmin(BaseUserAdmin):
    # inlines = (StudentProfileInline,CounselorProfileInline,EssaysInline,ActivityInline,SATInline,ACTInline,SubjectTestInline,TranscriptInline,LORInline,InviteInline)
    inlines = (StudentProfileInline, CounselorProfileInline, EssaysInline, TestingInLine, TranscriptInline, LORInline,
               InviteInline, NotesInline, DeadlineInLine, LinkInLine)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
