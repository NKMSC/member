from django.contrib import admin
from member.database.models import Activity,Code,Log,Section,User,UserTakePartInActivity

class UserAdmin(admin.ModelAdmin):
	raw_id_fields=('sec',)

admin.site.register(Activity)
admin.site.register(Code)
admin.site.register(Log)
admin.site.register(Section)
admin.site.register(User,UserAdmin)
admin.site.register(UserTakePartInActivity)