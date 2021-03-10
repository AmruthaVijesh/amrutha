from django.conf.urls import url
from django.urls import path
from blog import views

app_name='blog'
urlpatterns =[
    path('login/', views.login, name='blog_login'),
    path('logout/', views.logout, name='blog_logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
    url(r'^lousy_login/$', views.lousy_login, name='lousy_login'),
    url(r'^lousy_secret/$', views.lousy_secret, name='lousy_secret'),
    url(r'^lousy_logout/$', views.lousy_logout, name='lousy_logout'),
    url(r'^save_session_data/$', views.save_session_data, name='save_session_data'),
    url(r'^access_session_data/$', views.access_session_data, name='access_session_data'),
    url(r'^delete_session_data/$', views.delete_session_data, name='delete_session_data'),
    url(r'^test_delete/$', views.test_delete, name='test_delete'),
    url(r'^test_session/$', views.test_session, name='test_session'),
    url(r'^stop_tracking/$', views.stop_tracking, name='stop_tracking'),
    url(r'^track_user/$', views.track_user, name='track_user'),
    url(r'^cookie/$', views.test_cookie, name='cookie'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^blog/$', views.test_redirect, name='test_redirect'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    #url(r'^(?P<pk>\d+)/(?P<post_slug>[\w\d-]+)$', views.post_detail, name='post_detail'),
    path('<int:pk>', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    ]
