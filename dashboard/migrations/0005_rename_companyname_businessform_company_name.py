# Generated by Django 5.0 on 2023-12-14 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_businessform_contactname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessform',
            old_name='companyName',
            new_name='Company_Name',
        ),
    ]