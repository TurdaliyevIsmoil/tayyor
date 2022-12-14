# Generated by Django 4.0.4 on 2022-05-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applar', '0011_rename_name_company_contact_remove_company_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='contact',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='location',
        ),
        migrations.RemoveField(
            model_name='company',
            name='salary',
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.IntegerField(default=998901234567),
        ),
        migrations.AddField(
            model_name='company',
            name='place',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='email',
            field=models.EmailField(default='example@mail.com', max_length=254),
        ),
    ]
