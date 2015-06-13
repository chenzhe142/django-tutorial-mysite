from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	"""docstring for QuestionAdmin"""
	fields = ['pub_date', 'question_text']
	

# add admin interface to Question table
# update the order of items
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)