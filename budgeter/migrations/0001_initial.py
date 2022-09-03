# Generated by Django 4.1 on 2022-09-03 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no title', max_length=100)),
                ('budget_for', models.CharField(default='Misc.', max_length=100)),
                ('income', models.IntegerField(blank=True, default=0)),
                ('total', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('biller', models.CharField(max_length=100)),
                ('amount_planned', models.IntegerField(blank=True, default=0)),
                ('amount_actual', models.IntegerField(blank=True, default=0)),
                ('type_bill', models.CharField(choices=[('Misc', 'Miscellaneous'), ('Car', 'Car'), ('Elec', 'Electric'), ('Util', 'Utilites'), ('Food', 'Grocery'), ('Fun', 'Entertainment'), ('Kids', 'Kids'), ('Pets', 'Pets')], max_length=4)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='budgeter.budget')),
            ],
        ),
    ]