from django import forms
from .models import Course,Articles
class CourseForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(CourseForm, self).__init__(*args, **kwargs)
		for field in self.visible_fields():
			field.field.widget.attrs["class"] = "form-control"

	class Meta:
		model = Course
		exclude = ("author",)

class ArticleForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ArticleForm, self).__init__(*args, **kwargs)
		for field in self.visible_fields():
			field.field.widget.attrs["class"] = "form-control"

	class Meta:
		model = Articles
		exclude = ("author",)