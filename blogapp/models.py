from django.contrib.auth.models import AbstractUser
from django.db import models


# 用户模型
class MyUser(AbstractUser):
    tel = models.CharField(max_length=12)
    qq = models.IntegerField(null=True)
    # image = models.ImageField(upload_to='img')
    address = models.CharField(max_length=20)


# 文章分类模型
class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '文章分类'
        ordering = ['id']  # 排序显示，反排序则['-id']


# 用户头像
class Images(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='img')

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '图片'


# 标签模型
class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '标签'


# 文章模型
class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name='文章标题')
    content = models.TextField(verbose_name='内容')
    desc = models.CharField(max_length=20, verbose_name='文章简介')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    click_count = models.IntegerField(verbose_name='点击量', default=0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, verbose_name='所属用户')
    tag = models.ManyToManyField(Tag, through='ArticleTagRelation')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章'
        ordering = ['-date_publish', '-id']  # 最后发表的显示在前面


# 文章标签关系
class ArticleTagRelation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章标签关系'
        verbose_name_plural = verbose_name


# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='评论人')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='被评论文章')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                       blank=True, null=True, verbose_name='父评论')  # 自关联，blank为表单，null是数据库

    def __str__(self):
        return self.content[:10]

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
