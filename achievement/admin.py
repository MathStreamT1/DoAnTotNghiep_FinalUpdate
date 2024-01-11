
from django.contrib import admin
from .models import OLP

class OLPAdmin(admin.ModelAdmin):
    list_display = ['description', 'khoa', 'rank', 'system', 'year', 'certificate']
    search_fields = ['description', 'khoa','rank', 'system', 'year', 'certificate']
    list_filter = ['rank', 'system', 'year','certificate','khoa']

admin.site.register(OLP, OLPAdmin)



from .models import ICPC
admin.site.register(ICPC)

from .models import PROCON
class PROCONAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'result')
    list_filter = ('result','year',)
  
admin.site.register(PROCON, PROCONAdmin)
