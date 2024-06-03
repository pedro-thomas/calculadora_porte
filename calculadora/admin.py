# admin.py
from django.contrib import admin
from .models import WeaponInventory

class WeaponInventoryAdmin(admin.ModelAdmin):
    list_display = (
        'group', 
        'pistola_hk', 'pistola_hk_price',
        'pistola_glock', 'pistola_glock_price',
        'sub_mp5', 'sub_mp5_price',
        'sub_escorpion', 'sub_escorpion_price',
        'fuzil_nsr', 'fuzil_nsr_price',
        'fuzil_m4a4', 'fuzil_m4a4_price',
        'pistola_hk_municao', 'pistola_glock_municao', 'sub_mp5_municao', 'sub_escorpion_municao', 'fuzil_nsr_municao', 'fuzil_m4a4_municao',
        'total_value', 'treasurer_value'
    )

    readonly_fields = ('pistola_hk_price', 'pistola_glock_price', 'sub_mp5_price', 'sub_escorpion_price', 'fuzil_nsr_price', 'fuzil_m4a4_price')
    
    def pistola_hk_price(self, obj):
        return obj.pistola_hk_price
    pistola_hk_price.short_description = "Preço Pistola HK"
    
    def pistola_glock_price(self, obj):
        return obj.pistola_glock_price
    pistola_glock_price.short_description = "Preço Pistola Glock"
    
    def sub_mp5_price(self, obj):
        return obj.sub_mp5_price
    sub_mp5_price.short_description = "Preço Sub MP5"
    
    def sub_escorpion_price(self, obj):
        return obj.sub_escorpion_price
    sub_escorpion_price.short_description = "Preço Sub Escorpion"
    
    def fuzil_nsr_price(self, obj):
        return obj.fuzil_nsr_price
    fuzil_nsr_price.short_description = "Preço Fuzil NSR"
    
    def fuzil_m4a4_price(self, obj):
        return obj.fuzil_m4a4_price
    fuzil_m4a4_price.short_description = "Preço Fuzil M4A4"

admin.site.register(WeaponInventory, WeaponInventoryAdmin)
