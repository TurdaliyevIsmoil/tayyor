# Generated by Django 3.2.13 on 2022-06-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applar', '0020_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companiy', models.CharField(max_length=250, verbose_name='Companiy')),
                ('location', models.CharField(max_length=250, verbose_name='Location')),
                ('salary', models.CharField(max_length=250, verbose_name='Salary')),
            ],
        ),
    ]