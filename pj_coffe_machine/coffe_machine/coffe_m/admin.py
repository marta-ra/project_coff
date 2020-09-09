from django.contrib import admin
from . import models
# Register your models here.

#admin.site.register(models.Clients)
# admin.site.register(models.Point_coffemachine)
admin.site.register(models.Coffemachine)
admin.site.register(models.Visit)
admin.site.register(models.Point_address)
admin.site.register(models.Useful_code)
admin.site.register(models.Useful_docs)

@admin.register(models.Point_coffemachine)
class PointAdmin(admin.ModelAdmin):
    list_display = ('client_point', 'client_name', 'region', 'point_address', 'manager_name', 'manager_telephone', 'region',
                    #'description', 'code', 'model_machine', 'document'
                    )
    # list_filter = ('client_name',)
    # search_fields = ('client_address',)
    #ordering = ('next_t_check_date',)