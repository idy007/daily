# -*- coding:utf-8 -*-
#   Description: ---
#        Author: Lynn
#         Email: lgang219@gmail.com
#        Create: 2018-07-20 00:59:50
# Last Modified: 2018-08-22 09:55:00
#

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movie_index'),
    path('pages/<str:page_num>/', views.index_by_page, name='movie_index_by_page'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # 通过构造 URL 实现搜索
    # path('search/<str:movie_name>', views.movie_search, name='movie_search'),
    # navbar 中的 Form 搜索
    path('search/', views.movie_search_navbar, name='movie_search_navbar'),
    # 热搜榜
    path('resou/', views.movie_resou, name='movie_resou'),
    # 确认是否失效
    path('confirm_invalid/<int:movie_id>/<int:urlstate>', views.confirm_invalid, name='confirm_invalid'),
    # 报告失效
    path('invalid_url_report/<int:movie_id>/<int:urlstate>', views.invalid_url_report, name='invalid_url_report'),

    path('reset_form/<int:movie_id>', views.reset_form, name='reset_form'),
    path('reset_form/reset_valid/', views.reset_valid, name='reset_valid'),
]
