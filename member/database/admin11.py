from django.contrib import admin
from member.database.models import Activity,Code,Log,Section,User,UserTakePartInActivity

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publisher','publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	field = ('title','author','publisher',)    #orign admin enter will disdefault the option of publication_date
	filter_vertical = ('author',)
	list_filter = ('publication_date',)
	raw_id_fields=('publisher',)

admin.site.register(Activity)
admin.site.register(Code)
admin.site.register(Log)
admin.site.register(Section)
admin.site.register(User)
admin.site.register(UserTakePartInActivity)
#admin.site.register(Author,AuthorAdmin)
#admin.site.register(Book,BookAdmin)