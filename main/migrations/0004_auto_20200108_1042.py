# Generated by Django 3.0.2 on 2020-01-08 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200107_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnidetailmodel',
            name='Branch',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnidetailmodel',
            name='Contact',
            field=models.CharField(default=True, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnidetailmodel',
            name='Email',
            field=models.CharField(default=True, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumnidetailmodel',
            name='Image',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
    ]