from django.contrib import admin

from .models import QuestionDetails, QuestionCategories
# Register your models here.


class QuestionDetailsModelAdmin(admin.ModelAdmin):
	list_display = ["id", "Question_Type", "Created_Time", "Updated_Time","Tags"]
	
	class Meta:
		model = QuestionDetails



class QuestionCategoriesModelAdmin(admin.ModelAdmin):
	list_display = ["id", "Exam_Name", "Exam_Category", "Updated_Time"]
	
	class Meta:
		model = QuestionCategories

admin.site.register(QuestionDetails, QuestionDetailsModelAdmin)

admin.site.register(QuestionCategories, QuestionCategoriesModelAdmin)