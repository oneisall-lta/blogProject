from django.core.paginator import PageNotAnInteger, Paginator


# 通过页码返回相应的文章
def getblog_bypage(article_list, page_number):
    try:
        paginator = Paginator(article_list, 2)  # 实例化分页器对象
        page = paginator.page(page_number)  # 获取某一页的数据，以page对象封装,获取该page对象的记录则需要遍历该page对象
    except PageNotAnInteger:
        page = paginator.page(1)  # 返回第一页的对象

    return page
