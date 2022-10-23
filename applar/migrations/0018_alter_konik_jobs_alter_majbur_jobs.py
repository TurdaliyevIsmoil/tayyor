# Generated by Django 4.0.4 on 2022-05-24 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applar', '0017_remove_majbur_konikma_alter_majbur_jobs_konik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='konik',
            name='jobs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='konikm', to='applar.job'),
        ),
        migrations.AlterField(
            model_name='majbur',
            name='jobs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='majburi', to='applar.job'),
        ),
    ]