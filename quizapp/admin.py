from django.contrib import admin
from .models import Questions, Answer,Quiz,Result,Advertisement


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Questions, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Result)
admin.site.register(Advertisement)
