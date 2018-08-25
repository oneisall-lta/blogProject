from django import template

# 这个register变量是template.Library的实例，是所有注册标签和过滤器的数据结构
register = template.Library()


@register.filter(name='month_to_upper')
def month_to_upper(value):
    return ['一', '二', '三', '四', '五', '六', '七', '八',
            '九', '十', '十一', '十二'][value.month - 1]  # 列表索引切片
