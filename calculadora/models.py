from django.db import models

class WeaponInventory(models.Model):
    GROUP_CHOICES = [
        (1, 'Grupo 1'),
        (2, 'Grupo 2'),
        (3, 'Grupo 3'),
        (4, 'Grupo 4'),
        (5, 'Grupo 5'),
    ]

    group = models.IntegerField(choices=GROUP_CHOICES)

    # Campos para as armas
    pistola_hk = models.IntegerField(default=0)
    pistola_glock = models.IntegerField(default=0)
    sub_mp5 = models.IntegerField(default=0)
    sub_escorpion = models.IntegerField(default=0)
    fuzil_nsr = models.IntegerField(default=0)
    fuzil_m4a4 = models.IntegerField(default=0)

    # Campos para as munições
    pistola_hk_municao = models.IntegerField(default=0, verbose_name="Munição Pistola HK (Preço: 1000)")
    pistola_glock_municao = models.IntegerField(default=0, verbose_name="Munição Pistola Glock (Preço: 1400)")
    sub_mp5_municao = models.IntegerField(default=0, verbose_name="Munição Sub MP5 (Preço: 2000)")
    sub_escorpion_municao = models.IntegerField(default=0, verbose_name="Munição Sub Escorpion (Preço: 2500)")
    fuzil_nsr_municao = models.IntegerField(default=0, verbose_name="Munição Fuzil NSR (Preço: 3500)")
    fuzil_m4a4_municao = models.IntegerField(default=0, verbose_name="Munição Fuzil M4A4 (Preço: 4000)")

    # Novos campos para valores
    total_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Valor Total")
    treasurer_value = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Valor do Tesoureiro")

    def _get_weapon_prices(self):
        return {
            1: {'pistola_hk': 300000, 'pistola_glock': 720000, 'sub_mp5': 0, 'sub_escorpion': 0, 'fuzil_nsr': 0, 'fuzil_m4a4': 0,
                'pistola_hk_tesoureiro': 87500, 'pistola_glock_tesoureiro': 210000, 'sub_mp5_tesoureiro': 0, 'sub_escorpion_tesoureiro': 0, 'fuzil_nsr_tesoureiro': 0, 'fuzil_m4a4_tesoureiro': 0},
            2: {'pistola_hk': 250000, 'pistola_glock': 600000, 'sub_mp5': 1000000, 'sub_escorpion': 0, 'fuzil_nsr': 0, 'fuzil_m4a4': 0,
                'pistola_hk_tesoureiro': 62500, 'pistola_glock_tesoureiro': 150000, 'sub_mp5_tesoureiro': 250000, 'sub_escorpion_tesoureiro': 0, 'fuzil_nsr_tesoureiro': 0, 'fuzil_m4a4_tesoureiro': 0},
            3: {'pistola_hk': 225000, 'pistola_glock': 540000, 'sub_mp5': 900000, 'sub_escorpion': 1080000, 'fuzil_nsr': 0, 'fuzil_m4a4': 0,
                'pistola_hk_tesoureiro': 50000, 'pistola_glock_tesoureiro': 120000, 'sub_mp5_tesoureiro': 200000, 'sub_escorpion_tesoureiro': 240000, 'fuzil_nsr_tesoureiro': 0, 'fuzil_m4a4_tesoureiro': 0},
            4: {'pistola_hk': 200000, 'pistola_glock': 480000, 'sub_mp5': 800000, 'sub_escorpion': 960000, 'fuzil_nsr': 1280000, 'fuzil_m4a4': 0,
                'pistola_hk_tesoureiro': 37500, 'pistola_glock_tesoureiro': 90000, 'sub_mp5_tesoureiro': 150000, 'sub_escorpion_tesoureiro': 180000, 'fuzil_nsr_tesoureiro': 240000, 'fuzil_m4a4_tesoureiro': 0},
            5: {'pistola_hk': 175000, 'pistola_glock': 420000, 'sub_mp5': 700000, 'sub_escorpion': 840000, 'fuzil_nsr': 1120000, 'fuzil_m4a4': 2520000,
                'pistola_hk_tesoureiro': 25000, 'pistola_glock_tesoureiro': 60000, 'sub_mp5_tesoureiro': 100000, 'sub_escorpion_tesoureiro': 120000, 'fuzil_nsr_tesoureiro': 160000, 'fuzil_m4a4_tesoureiro': 360000},
        }

    def save(self, *args, **kwargs):
        prices = self._get_weapon_prices()
        group_prices = prices[self.group]

        total_value = (
            self.pistola_hk * group_prices['pistola_hk'] +
            self.pistola_glock * group_prices['pistola_glock'] +
            self.sub_mp5 * group_prices['sub_mp5'] +
            self.sub_escorpion * group_prices['sub_escorpion'] +
            self.fuzil_nsr * group_prices['fuzil_nsr'] +
            self.fuzil_m4a4 * group_prices['fuzil_m4a4'] +
            self.pistola_hk_municao * 1000 +
            self.pistola_glock_municao * 1400 +
            self.sub_mp5_municao * 2000 +
            self.sub_escorpion_municao * 2500 +
            self.fuzil_nsr_municao * 3500 +
            self.fuzil_m4a4_municao * 4000
        )

        treasurer_value = (
            self.pistola_hk * group_prices['pistola_hk_tesoureiro'] +
            self.pistola_glock * group_prices['pistola_glock_tesoureiro'] +
            self.sub_mp5 * group_prices['sub_mp5_tesoureiro'] +
            self.sub_escorpion * group_prices['sub_escorpion_tesoureiro'] +
            self.fuzil_nsr * group_prices['fuzil_nsr_tesoureiro'] +
            self.fuzil_m4a4 * group_prices['fuzil_m4a4_tesoureiro']
        )

        self.total_value = total_value
        self.treasurer_value = treasurer_value

        super().save(*args, **kwargs)


class Sale(models.Model):
    weapon_inventory = models.ForeignKey(WeaponInventory, on_delete=models.CASCADE)
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    treasurer_value = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda {self.id} - Total: R${self.total_value} - Tesoureiro: R${self.treasurer_value}"
