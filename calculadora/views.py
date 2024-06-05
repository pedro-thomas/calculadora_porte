from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import WeaponInventoryForm
from .models import Sale, WeaponInventory

def register_sale(request):
    if request.method == 'POST':
        weapon_form = WeaponInventoryForm(request.POST)
        buyer_id = request.POST.get('buyer_id')
        if weapon_form.is_valid() and buyer_id:
            weapon_inventory = weapon_form.save()
            sale = Sale.objects.create(
                weapon_inventory=weapon_inventory,
                buyer_id=buyer_id,
                total_value=weapon_inventory.total_value,
                treasurer_value=weapon_inventory.treasurer_value
            )
            return redirect('sale_report', sale_id=sale.id)
    else:
        weapon_form = WeaponInventoryForm()

    return render(request, 'register_sale.html', {'weapon_form': weapon_form})

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'sale_list.html', {'sales': sales})

def calculate_totals(request):
    if request.method == 'POST':
        group = int(request.POST.get('group'))
        pistola_hk = int(request.POST.get('pistola_hk', 0))
        pistola_glock = int(request.POST.get('pistola_glock', 0))
        sub_mp5 = int(request.POST.get('sub_mp5', 0))
        sub_escorpion = int(request.POST.get('sub_escorpion', 0))
        fuzil_nsr = int(request.POST.get('fuzil_nsr', 0))
        fuzil_m4a4 = int(request.POST.get('fuzil_m4a4', 0))
        pistola_hk_municao = int(request.POST.get('pistola_hk_municao', 0))
        pistola_glock_municao = int(request.POST.get('pistola_glock_municao', 0))
        sub_mp5_municao = int(request.POST.get('sub_mp5_municao', 0))
        sub_escorpion_municao = int(request.POST.get('sub_escorpion_municao', 0))
        fuzil_nsr_municao = int(request.POST.get('fuzil_nsr_municao', 0))
        fuzil_m4a4_municao = int(request.POST.get('fuzil_m4a4_municao', 0))

        weapon_inventory = WeaponInventory(group=group)
        prices = weapon_inventory._get_weapon_prices()
        group_prices = prices[group]

        total_value = (
            pistola_hk * group_prices['pistola_hk'] +
            pistola_glock * group_prices['pistola_glock'] +
            sub_mp5 * group_prices['sub_mp5'] +
            sub_escorpion * group_prices['sub_escorpion'] +
            fuzil_nsr * group_prices['fuzil_nsr'] +
            fuzil_m4a4 * group_prices['fuzil_m4a4'] +
            pistola_hk_municao * 1000 +
            pistola_glock_municao * 1400 +
            sub_mp5_municao * 2000 +
            sub_escorpion_municao * 2500 +
            fuzil_nsr_municao * 3500 +
            fuzil_m4a4_municao * 4000
        )

        treasurer_value = (
            pistola_hk * group_prices['pistola_hk_tesoureiro'] +
            pistola_glock * group_prices['pistola_glock_tesoureiro'] +
            sub_mp5 * group_prices['sub_mp5_tesoureiro'] +
            sub_escorpion * group_prices['sub_escorpion_tesoureiro'] +
            fuzil_nsr * group_prices['fuzil_nsr_tesoureiro'] +
            fuzil_m4a4 * group_prices['fuzil_m4a4_tesoureiro']
        )

        return JsonResponse({
            'total_value': total_value,
            'treasurer_value': treasurer_value
        })

def sale_report(request, sale_id):
    sale = get_object_or_404(Sale, id=sale_id)
    context = {
        'sale': sale,
        'porte': sale.get_porte(),
        'vendido': sale.get_vendido()
    }
    return render(request, 'sale_report.html', context)