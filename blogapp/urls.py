from django.urls import path

from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index,name='main'),
    path('category_artical/<cid>/', views.category_article, name='category_artical'),
    path('page_articles/', views.article_page, name='page_article'),
    path('showart/', views.getarticle_byid, name='showart'),
    path('goreg/',views.reg, name='goreg'),
    path('gologin/',views.login,name='gologin'),
    path('logout/',views.logout,name='logout'),
]
