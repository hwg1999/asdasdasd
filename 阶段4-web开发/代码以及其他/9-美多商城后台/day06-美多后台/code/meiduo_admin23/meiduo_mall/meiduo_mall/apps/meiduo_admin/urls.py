from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from .views import statistical
urlpatterns = [
    # 登录
    url(r'^authorizations/$', obtain_jwt_token),
    # --------------  数据统计 -----------------
    # 用户总量
    url(r'^statistical/total_count/$', statistical.UserCountView.as_view()),
    # 日增用户
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # 日活用户
    url(r'^statistical/day_active/$', statistical.UserDayActiveCountView.as_view()),
    # 下单用户
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersCountView.as_view()),
    # 月增用户
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),

    url(r'^statistical/goods_day_views/$', statistical.UserGoodsCountView.as_view()),
]




