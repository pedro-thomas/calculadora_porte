from django import forms
from .models import WeaponInventory

class WeaponInventoryForm(forms.ModelForm):
    class Meta:
        model = WeaponInventory
        fields = [
            'group',
            'pistola_hk', 'pistola_glock', 'sub_mp5', 'sub_escorpion', 'fuzil_nsr', 'fuzil_m4a4',
            'pistola_hk_municao', 'pistola_glock_municao', 'sub_mp5_municao', 'sub_escorpion_municao', 'fuzil_nsr_municao', 'fuzil_m4a4_municao'
        ]

    @property
    def pistola_hk_price(self):
        return {1: 300000, 2: 250000, 3: 225000, 4: 200000, 5: 175000}

    @property
    def pistola_glock_price(self):
        return {1: 720000, 2: 600000, 3: 540000, 4: 480000, 5: 420000}

    @property
    def sub_mp5_price(self):
        return {1: 0, 2: 1000000, 3: 900000, 4: 800000, 5: 700000}

    @property
    def sub_escorpion_price(self):
        return {1: 0, 2: 0, 3: 1080000, 4: 960000, 5: 840000}

    @property
    def fuzil_nsr_price(self):
        return {1: 0, 2: 0, 3: 0, 4: 1280000, 5: 1120000}

    @property
    def fuzil_m4a4_price(self):
        return {1: 0, 2: 0, 3: 0, 4: 0, 5: 2520000}

    def get_weapon_prices(self):
        return {
            'pistola_hk': self.pistola_hk_price,
            'pistola_glock': self.pistola_glock_price,
            'sub_mp5': self.sub_mp5_price,
            'sub_escorpion': self.sub_escorpion_price,
            'fuzil_nsr': self.fuzil_nsr_price,
            'fuzil_m4a4': self.fuzil_m4a4_price,
        }
