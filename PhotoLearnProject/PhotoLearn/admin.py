from django.contrib import admin
from .models import Course, UserCustom, Articles
#from rangefilter.filters import DateRangeFilter,DateTimeRangeFilter
# Register your models here.

class UserCustomAdmin(admin.ModelAdmin):
	list_display = ("name", "surname")

	def has_change_permission(self,request,obj = None):
		if obj is not None and obj.user == request.user:
			return True
		return False


admin.site.register(UserCustom, UserCustomAdmin)
"""
class UserBlocksAdmin(admin.ModelAdmin):
	list_display = ("userThatIsBlocking","blockedUser",)
admin.site.register(UserBlocks,UserBlocksAdmin)
"""

"""
class PostCommentAdmin(admin.StackedInline):
	model = Course
	extra = 0
"""
class CourseAdmin(admin.ModelAdmin):
	list_display=("title", "author",)
	list_filter = ("date_created",)
	search_fields = ("title", "content")
#	inlines = [PostCommentAdmin, ]

	def get_readonly_fields(self, request, obj=None):
		if obj is not None and obj.author == request.user:
			return []
		if obj is None:
			return []
		return [
			"author",
			"title",
			"content",
			"files",
			"date_created",
			"last_updated",
		]
	def has_delete_permission(self, request, obj=None):
		if obj is not None and request.user == obj.author:
			return True
		return False
	def has_change_permission(self,request, obj = None):
		if obj and (request.user == obj.author):
			return True
		return False
	def has_view_permission(self, request, obj=None):
		return True
	def has_add_permission(self,request,obj = None):
		return True
"""
	def get_queryset(self,request):
		qs = super(BlogPostAdmin,self).get_queryset(request)
		usersThatBlockedUs = UserBlocks.objects.filter(blockedUser=request.user).values_list("userThatIsBlocking")
		qs = qs.exclude(author__in = usersThatBlockedUs)
		return qs
"""
admin.site.register(Course,CourseAdmin)

class ArticleAdmin(admin.ModelAdmin):
	list_display=("title", "author",)
	list_filter = ("date_created",)
	search_fields = ("title", "content")
#	inlines = [PostCommentAdmin, ]

	def get_readonly_fields(self, request, obj=None):
		if obj is not None and obj.author == request.user:
			return []
		if obj is None:
			return []
		return [
			"author",
			"title",
			"content",
			"date_created",
			"last_updated",
		]
	def has_delete_permission(self, request, obj=None):
		if obj is not None and request.user == obj.author:
			return True
		return False
	def has_change_permission(self,request, obj = None):
		if obj and (request.user == obj.author):
			return True
		return False
	def has_view_permission(self, request, obj=None):
		return True
	def has_add_permission(self,request,obj = None):
		return True
"""
	def get_queryset(self,request):
		qs = super(BlogPostAdmin,self).get_queryset(request)
		usersThatBlockedUs = UserBlocks.objects.filter(blockedUser=request.user).values_list("userThatIsBlocking")
		qs = qs.exclude(author__in = usersThatBlockedUs)
		return qs
"""
admin.site.register(Articles,ArticleAdmin)