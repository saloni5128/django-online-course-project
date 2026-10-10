from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Register your models here
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
