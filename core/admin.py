"""
    This is where you register models so that they are viewable and editable in the built in Django admin page.
"""
from django.contrib import admin

# Register your models here.
from core.models import User, GlobalMenu, ItemInBill, Questionnaire, AnsweredQuestionnaire, Review

admin.site.register(User)
admin.site.register(GlobalMenu)
admin.site.register(ItemInBill)
admin.site.register(Questionnaire)
admin.site.register(AnsweredQuestionnaire)
admin.site.register(Review)