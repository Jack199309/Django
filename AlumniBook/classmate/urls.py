from django.urls import path,include
import xadmin
from.views import *
urlpatterns = [
    path('index/',IndexView),
    path('kou/',kouView),
    # path('regist/',RegisterView),#注册页面路径

]