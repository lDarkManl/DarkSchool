# Generated by Django 4.2.15 on 2024-09-04 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название курса')),
                ('price', models.IntegerField(verbose_name='Цена курса')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название предмета')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(verbose_name='Ссылка на видео')),
                ('title', models.CharField(max_length=100, verbose_name='Название урока')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAnswerLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ответ на задание')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentAnswerWebinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ответ на задание')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(verbose_name='Ссылка на видео')),
                ('title', models.CharField(max_length=100, verbose_name='Название вебинара')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webinars', to='courses.course', verbose_name='course')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
