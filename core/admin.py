from django.contrib import admin

# Register your models here.
from core.models import User, GlobalMenu, ItemInBill, Questionnaire, AnsweredQuestionnaire, Review, StylistMenu

admin.site.register(User)
admin.site.register(GlobalMenu)
admin.site.register(StylistMenu)
admin.site.register(ItemInBill)
admin.site.register(Questionnaire)
admin.site.register(AnsweredQuestionnaire)
admin.site.register(Review)