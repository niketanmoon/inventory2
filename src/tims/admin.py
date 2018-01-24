from django.contrib import admin
from . models import Computer
# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
	class Meta:
		model = Computer
	list_display = ('ip_address','SerialKey','HostName','BrandName','OsName','OsVersion','Processor','Ram','ExternalStorage','Location')
	list_filter = ['ip_address']
	search_fields = ['ip_address']	


admin.site.register(Computer, ComputerAdmin)
