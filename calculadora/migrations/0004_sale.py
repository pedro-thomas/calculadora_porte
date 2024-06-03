# Generated by Django 5.0.6 on 2024-06-02 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0003_alter_weaponinventory_fuzil_m4a4_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('treasurer_value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('weapon_inventory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calculadora.weaponinventory')),
            ],
        ),
    ]