# Generated by Django 2.1.7 on 2019-03-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmate', '0004_auto_20190318_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classinfo',
            name='classNo',
            field=models.CharField(max_length=50, verbose_name='班级编号'),
        ),
    ]
