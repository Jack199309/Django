# Generated by Django 2.1.7 on 2019-03-18 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classmate', '0006_auto_20190318_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_name',
        ),
        migrations.AddField(
            model_name='news',
            name='p_name',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='classmate.PersonalInfo', verbose_name='用户姓名'),
            preserve_default=False,
        ),
    ]