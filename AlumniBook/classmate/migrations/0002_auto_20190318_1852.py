# Generated by Django 2.1.7 on 2019-03-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classmate', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodthings',
            options={'verbose_name': '好物表', 'verbose_name_plural': '好物表'},
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='sex',
            field=models.CharField(choices=[(1, '男'), (2, 'nv')], max_length=50),
        ),
    ]