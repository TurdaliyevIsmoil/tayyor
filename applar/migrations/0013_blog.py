# Generated by Django 4.0.4 on 2022-05-21 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applar', '0012_delete_about_delete_testimonial_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='blog_images')),
            ],
        ),
    ]