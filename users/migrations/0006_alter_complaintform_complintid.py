# Generated by Django 5.0 on 2023-12-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_complaintform_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaintform',
            name='ComplintId',
            field=models.CharField(default='CM56214370', max_length=10, null=True),
        ),
    ]