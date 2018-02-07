from django.urls import path
from . import views

urlpatterns=[
    path('article-column/',views.acticle_column,name="article_column"),
    path('article_add/',views.article_add,name="article_add"),
    path('rename-column/',views.rename_article_column,name="rename_article_column"),
    path('del-column/',views.del_article_column,name="del_article_column")
]