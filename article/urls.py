from django.urls import path
from . import views

urlpatterns=[
    path('article-column/',views.acticle_column,name="article_column"),
    path('article_add/',views.article_add,name="article_add"),
    path('rename-column/',views.rename_article_column,name="rename_article_column"),
    path('del-column/',views.del_article_column,name="del_article_column"),
    path('article-post/',views.article_post,name="article_post"),
    path('article-list/',views.article_list,name="article_list"),
    path('article-detail/<int:id>/<str:slug>',views.article_detail,name="article_detail"),
    path('del-article/',views.del_article,name="del_article")
]