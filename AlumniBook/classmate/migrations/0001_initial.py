# Generated by Django 2.1.7 on 2019-03-18 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_type', models.CharField(max_length=50, verbose_name='系别')),
                ('teacherOne', models.CharField(max_length=50)),
                ('classcount', models.IntegerField(verbose_name='班级人数')),
            ],
            options={
                'verbose_name': '班级信息表',
                'verbose_name_plural': '班级信息表',
            },
        ),
        migrations.CreateModel(
            name='classUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=50, verbose_name='用户账号')),
                ('password', models.CharField(max_length=50, verbose_name='密码')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.CharField(max_length=100, verbose_name='评论内容')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '评论回复表',
                'verbose_name_plural': '评论回复表',
            },
        ),
        migrations.CreateModel(
            name='god',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('god_score', models.IntegerField(default=0, verbose_name='积分')),
            ],
            options={
                'verbose_name': '大神表',
                'verbose_name_plural': '大神表',
            },
        ),
        migrations.CreateModel(
            name='goodthings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('things_name', models.CharField(max_length=50, verbose_name='物品名')),
                ('things_des', models.TextField(verbose_name='物品描述')),
                ('things_price', models.FloatField(default=0.0, verbose_name='物品价格')),
                ('things_time', models.DateTimeField(auto_now_add=True, verbose_name='上线时间')),
                ('things_reason', models.TextField(verbose_name='分享理由')),
                ('things_conut', models.IntegerField(verbose_name='点赞次数')),
                ('things_paper', models.IntegerField(verbose_name='阅读数量')),
                ('good_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.classUser', verbose_name='用户名')),
            ],
            options={
                'verbose_name': '大神表',
                'verbose_name_plural': '大神表',
            },
        ),
        migrations.CreateModel(
            name='MaliList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classNo', models.IntegerField(verbose_name='班级编号')),
                ('personalid', models.IntegerField(verbose_name='个人id')),
            ],
            options={
                'verbose_name': '通讯录表',
                'verbose_name_plural': '通讯录表',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_type', models.CharField(choices=[(1, '动态'), (2, '技术文章'), (3, '难题')], max_length=50)),
                ('newsimg', models.ImageField(upload_to='stumg', verbose_name='动态照片')),
                ('news_content', models.TextField(verbose_name='内容')),
                ('news_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('news_Praisepoints', models.IntegerField(verbose_name='点赞数')),
                ('news_paper', models.IntegerField(verbose_name='阅读数量')),
                ('news_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.classUser', verbose_name='用户姓名')),
            ],
            options={
                'verbose_name': '动态表',
                'verbose_name_plural': '动态表',
            },
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=50, verbose_name='性别')),
                ('brithday', models.DateField(verbose_name='用户生日')),
                ('personaladdr', models.CharField(max_length=100, verbose_name='用户地址')),
                ('phone', models.IntegerField(verbose_name='用户电话')),
                ('Emaliaddr', models.EmailField(max_length=100, verbose_name='用户邮箱')),
                ('classmessage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.classinfo', verbose_name='班级信息')),
                ('p_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.classUser', verbose_name='用户姓名')),
            ],
            options={
                'verbose_name': '个人信息表',
                'verbose_name_plural': '个人信息表',
            },
        ),
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_load', models.ImageField(upload_to='stumg', verbose_name='相册图片')),
                ('picture_des', models.TextField(verbose_name='图片详情')),
                ('picture_time', models.DateTimeField(auto_now_add=True, verbose_name='图片上传时间')),
                ('picture_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.MaliList', verbose_name='班级编号')),
                ('picture_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.PersonalInfo', verbose_name='个人')),
            ],
            options={
                'verbose_name': '相册表',
                'verbose_name_plural': '相册表',
            },
        ),
        migrations.CreateModel(
            name='schoolm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.DateTimeField(max_length=50, verbose_name='校名')),
                ('schoolimg', models.ImageField(upload_to='stumg', verbose_name='校徽')),
                ('schooladdr', models.CharField(max_length=50, verbose_name='校址')),
            ],
            options={
                'verbose_name': '学校表',
                'verbose_name_plural': '学校表',
            },
        ),
        migrations.AddField(
            model_name='god',
            name='classid',
            field=models.ForeignKey(on_delete=models.Model, to='classmate.MaliList'),
        ),
        migrations.AddField(
            model_name='god',
            name='god_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.classUser'),
        ),
        migrations.AddField(
            model_name='comment',
            name='c_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dd', to='classmate.news', verbose_name='评论目标用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cc', to='classmate.classUser', verbose_name='评论用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classmate.news', verbose_name='内容'),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='classNo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bb', to='classmate.MaliList', verbose_name='班级编号'),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='schoolname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aa', to='classmate.schoolm', verbose_name='校名'),
        ),
    ]