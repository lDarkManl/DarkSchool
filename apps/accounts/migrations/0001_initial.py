# Generated by Django 4.2.15 on 2024-08-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('info', models.TextField(verbose_name='Информация о человеке')),
                ('details', models.TextField(verbose_name='Реквизиты для оплаты')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeacherAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('info', models.TextField(verbose_name='Информация о человеке')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]