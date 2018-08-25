from DjangoProject01 import settings
from blogapp.models import Category


def global_settings(request):
    BLOG_NAME = settings.BLOG_NAME  # 读取settings中的配置BLOG_NAME的值
    BLOG_DESC = settings.BLOG_DESC
    category_list = Category.objects.all()
    return locals()
