from django.contrib import admin

# Register your models here.
from core.models import User, Menu, Bill, Questionnaire, AnsweredQuestionnaire

admin.site.register(User)
admin.site.register(Menu)
admin.site.register(Bill)
admin.site.register(Questionnaire)
admin.site.register(AnsweredQuestionnaire)
