from django.contrib import admin
from .models import ComprarArticulo
# Register your models here.

class AdminComprarArticulo(admin.ModelAdmin):
	list_display = ["__unicode__", "tipo_de_comida", "color"]
	class Meta:
		model = ComprarArticulo 


admin.site.register(ComprarArticulo, AdminComprarArticulo)