import xadmin
from xadmin.views import *
from .models import *

class classUserAdmin(object):
    list_display=['id','account','password','time']
    pass

class schoolmAdmin(object):
    list_display=['id','schoolname','schoolimg','schooladdr']


class classinfoAdmin(object):
    list_display=['id','schoolname','class_type','classNo','teacherOne','classcount']
    pass

class MalistAdmin(object):
    list_display=['id','classNo','personalid']
    pass

class PersonalInfoAdmin(object):
    list_display=['id','p_id','p_name','sex','brithday','personaladdr','phone','Emaliaddr','classmessage']
    pass

class newsAdmin(object):
    list_display=['id','p_name','news_type','newsimg','news_content','news_time','news_Praisepoints','news_paper']
    pass

class commentAdmin(object):
    list_display=['id','content','comment_body','comment_time','comment_name','c_name']
    pass

class godAdmin(object):
    list_display=['id','classNo','god_name','god_score']
    pass

class goodthingsAdmin(object):
    list_display=['id','good_name','things_name','things_des','things_price','things_time','things_reason','things_conut','things_paper']
    pass

class pictureAdmin(object):
    list_diaplay=['id','picture_class','picture_person','picture_load','picture_des','picture_time']
    pass


class BaseSet(object):
    enable_themes = True  # 启用主题
    use_bootswatch = True  # 启用更多主题
    pass

class CommSet(object):
    title = '欢迎登入通讯录后台'  # 登录提示
    site_title = '通讯录管理后台'
    site_footer = '班级通讯录'
    menu_style = 'accordion'  # 菜单样式：折叠
    pass


#配置项
# xadmin.site.register()
xadmin.site.register(BaseAdminView,BaseSet)
xadmin.site.register(CommAdminView,CommSet)


xadmin.site.register(classUser,classUserAdmin)
xadmin.site.register(schoolm,schoolmAdmin)
xadmin.site.register(classinfo,classinfoAdmin)
xadmin.site.register(MaliList, MalistAdmin)
xadmin.site.register(PersonalInfo,PersonalInfoAdmin)
xadmin.site.register(news,newsAdmin)
xadmin.site.register(comment,commentAdmin)
xadmin.site.register(god,godAdmin)
xadmin.site.register(goodthings,goodthingsAdmin)
xadmin.site.register(picture,pictureAdmin)
