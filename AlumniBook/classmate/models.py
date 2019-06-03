from django.db import models

# Create your models here.

class classUser(models.Model):
    account=models.CharField(max_length=50,verbose_name='用户账号')
    password=models.CharField(max_length=50,verbose_name='密码')
    time=models.DateTimeField(auto_now_add=True,verbose_name='注册时间')
    def __str__(self):
        return self.account
    pass
    class Meta:
        verbose_name='用户账号表'
        verbose_name_plural=verbose_name

class schoolm(models.Model):
    schoolname=models.CharField(max_length=50,verbose_name='校名')
    schoolimg=models.ImageField(upload_to='stumg',verbose_name='校徽')
    schooladdr=models.CharField(max_length=50,verbose_name='校址')
    def  __str__(self):
        return self.schoolname
    class Meta:
        verbose_name = '学校信息表'
        verbose_name_plural = verbose_name
    pass
class classinfo(models.Model):
    schoolname=models.ForeignKey('schoolm',verbose_name='校名',on_delete=models.CASCADE,related_name='aa')
    class_type=models.CharField(max_length=50,verbose_name='系别')
    classNo=models.CharField(max_length=50,verbose_name='班级编号')
    teacherOne=models.CharField(max_length=50,)
    classcount=models.IntegerField(verbose_name='班级人数',default=0)
    def __str__(self):
        return self.classNo
    class Meta:
        verbose_name = '班级信息表'
        verbose_name_plural = verbose_name
        pass
    pass

class MaliList(models.Model):
    classNo=models.ForeignKey('classinfo',verbose_name='班级编号',on_delete=models.CASCADE)
    personalid=models.IntegerField(verbose_name='个人id')
    def __str(self):
        return self.classNo
    class Meta:
        verbose_name = '通讯录表'
        verbose_name_plural = verbose_name
        pass
    pass

class PersonalInfo(models.Model):
    p_id = models.ForeignKey('classUser', verbose_name='用户账号', on_delete=models.CASCADE)
    p_name = models.CharField(max_length=50,verbose_name='用户姓名')
    sex=models.CharField(max_length=50,choices=(('1','男'),('2','女')))
    brithday=models.DateField(verbose_name='用户生日')
    personaladdr=models.CharField(max_length=100,verbose_name='用户地址')
    phone=models.CharField(max_length=50,verbose_name='用户电话')
    Emaliaddr=models.EmailField(max_length=100,verbose_name='用户邮箱')
    classNo=models.ForeignKey('classinfo',verbose_name='班级信息',on_delete=models.CASCADE)
    def __str__(self):
        return self.p_name
    class Meta:
        verbose_name = '个人信息表'
        verbose_name_plural = verbose_name
        pass
    pass

class news(models.Model):
    p_name=models.ForeignKey('classUser',verbose_name='用户姓名',on_delete=models.CASCADE)
    news_type=models.CharField(max_length=50,choices=(('1','动态'),('2','技术文章'),('3','难题')))
    newsimg=models.ImageField(upload_to='stumg',verbose_name='动态照片')
    news_content=models.TextField(verbose_name='内容')
    news_time=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    news_Praisepoints=models.IntegerField(verbose_name='点赞数')
    news_paper=models.IntegerField(verbose_name='阅读数量')
    class Meta:
        verbose_name = '动态表'
        verbose_name_plural = verbose_name
        pass
    pass

class comment(models.Model):
    content=models.ForeignKey('news',verbose_name='内容',on_delete=models.CASCADE)
    comment_body=models.CharField(max_length=100,verbose_name='评论内容')
    comment_time=models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    comment_name=models.ForeignKey('classUser',verbose_name='评论用户',on_delete=models.CASCADE,related_name='cc')
    c_name=models.ForeignKey('news',verbose_name='评论',on_delete=models.CASCADE,related_name='dd')
    class Meta:
        verbose_name = '评论回复表'
        verbose_name_plural = verbose_name
        pass
    pass


class god(models.Model):
    classNo=models.ForeignKey('MaliList',on_delete=models.Model)
    god_name=models.ForeignKey('classUser',on_delete=models.CASCADE)
    god_score=models.IntegerField(verbose_name='积分',default=0)
    class Meta:
        verbose_name = '大神表'
        verbose_name_plural = verbose_name
        pass
    pass

class goodthings(models.Model):
    good_name=models.ForeignKey('classUser',verbose_name='用户名',on_delete=models.CASCADE)
    things_name=models.CharField(max_length=50,verbose_name='物品名')
    things_des=models.TextField(verbose_name='物品描述')
    things_price=models.FloatField(default=0.0,verbose_name='物品价格')
    things_time=models.DateTimeField(auto_now_add=True,verbose_name='上线时间')
    things_reason=models.TextField(verbose_name='分享理由')
    things_conut=models.IntegerField(verbose_name='点赞次数')
    things_paper=models.IntegerField(verbose_name='阅读数量')
    class Meta:
        verbose_name = '好物表'
        verbose_name_plural = verbose_name
        pass
    pass

class picture(models.Model):
    picture_class=models.ForeignKey('MaliList',verbose_name='班级编号',on_delete=models.CASCADE)
    picture_person=models.ForeignKey('PersonalInfo',verbose_name='个人',on_delete=models.CASCADE)
    picture_load=models.ImageField(upload_to='stumg',verbose_name='相册图片')
    picture_des=models.TextField(verbose_name='图片详情')
    picture_time=models.DateTimeField(auto_now_add=True,verbose_name='图片上传时间')
    class Meta:
        verbose_name = '相册表'
        verbose_name_plural = verbose_name
        pass
    pass



