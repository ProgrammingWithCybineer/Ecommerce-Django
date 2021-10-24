from django.contrib import admin
from .models import Products
from .models import Order
# Register your models here.
admin.site.site_header = "Dress Me Up Plus"
admin.site.site_title = "Dress Me Up Plus Admin Site"
admin.site.index_title = "Manage Dress Me Up Plus Shoping"

class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_clothes(self,request,queryset):
        queryset.update(category="clothes")

    change_category_to_clothes.short_description = "Default Category"
    list_display = ("title", "price", "color", "size", "item_detail", "category", "material_made", "image" )
    search_fields = ['title', 'size','category']
    actions = ("change_category_to_clothes", )
    #To only display fields you want to see in admin panel
    #fields = ("title", "price",)
    list_editable = ('price','category',)

admin.site.register(Products,ProductAdmin)
admin.site.register(Order)