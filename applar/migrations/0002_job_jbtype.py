# Generated by Django 4.0.4 on 2022-05-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='jbtype',
            field=models.CharField(blank=True, choices=[('Intership', 'Intership'), ('Part-time', 'Part-time'), ('Urgent', 'Urgent')], max_length=255, null=True),
        ),
    ]
