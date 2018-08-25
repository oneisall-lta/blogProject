from django.contrib import admin

# Register your models here.
from blogapp.models import *

admin.site.register([Article, Category, MyUser, Images, Tag, ArticleTagRelation, Comment])
