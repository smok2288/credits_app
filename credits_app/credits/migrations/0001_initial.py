# Generated by Django 5.0.2 on 2024-08-18 10:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата ввода записи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата деактивации записи')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер контракта')),
            ],
            options={
                'verbose_name': 'Номер контракта',
                'verbose_name_plural': 'Номера контрактов',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата ввода записи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата деактивации записи')),
                ('name', models.CharField(max_length=250, verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производители',
            },
        ),
        migrations.CreateModel(
            name='LoanRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата ввода записи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата деактивации записи')),
                ('number', models.CharField(max_length=250, verbose_name='Номер кредитной заявки')),
                ('contract', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loan_request', to='credits.contract', verbose_name='Контракт')),
            ],
            options={
                'verbose_name': 'Кредитная заявка',
                'verbose_name_plural': 'Кредитные заявки',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата редактирования')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата ввода записи')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата деактивации записи')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование товара')),
                ('loan_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='credits.loanrequest', verbose_name='Кредитная заявка')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='credits.manufacturer', verbose_name='Производитель')),
            ],
            options={
                'verbose_name': 'Наименование товара',
                'verbose_name_plural': 'Наименование товаров',
            },
        ),
    ]
