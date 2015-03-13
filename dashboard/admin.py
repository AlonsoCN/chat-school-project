from django.contrib import admin
from .models import Course
from .models import Course_publication
from .models import Publication
from .models import Section
from .models import UserProfile
from .models import User_section
from .models import User_publication


class UserProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('user', 'dni', ('address', 'phone', 'image'),
              ('privilege', 'user_type', 'is_deleted'))
    list_display = ('user', 'address', 'dni', 'privilege', 'user_type')
    list_filter = ['privilege', 'is_deleted']
    search_fields = ['user', 'address', 'dni', 'privilege', 'user_type']
    ordering = ['user__last_name']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Publication)
admin.site.register(Course)
admin.site.register(User_section)
admin.site.register(User_publication)
admin.site.register(Course_publication)
admin.site.register(Section)
