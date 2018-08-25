from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def create_childcomment_html(child_comment_dict, margin_left):
    html = ''
    for k, v in child_comment_dict.items():
        html += "<div style='margin-left:%spx'>" % margin_left + "<p style='color:blue;border:0.5px dotted gray;display:inline'>" +\
                k.date_publish.strftime('%Y-%m-%d') + "&emsp;" + k.user.username + '</p>' + "&emsp;" + k.content + '</div>'
        if v:
            html += create_childcomment_html(v, margin_left + 20)
    return html


# 从评论树中寻找某个评论的父评论
def find_parent_comment(comment_tree, comment):
    for p in comment_tree:  # 遍历评论树  ,items()返回(键，值)元组数组
        if p == comment.parent_comment:  # 如果在评论树中找到了该评论对象的父评论
            comment_tree[p][comment] = {}  # 将父评论对象与子评论对象关联
            break
        else:
            find_parent_comment(comment_tree[p], comment)  # 递归调用


@register.simple_tag
def create_comment_tree(comments):
    comment_tree = {}  # 将要填充的评论树
    for comment in comments:  # 遍历该文章下的所有评论
        if comment.parent_comment is None:  # 父评论为None，说明是一级评论
            comment_tree[comment] = {}  # 将一级评论作为评论树的键
        else:
            find_parent_comment(comment_tree, comment)

    html = '<div>'
    margin_left = 0

    for k, v in comment_tree.items():
        html += "<div>" + "<p style='color:blue;border:0.5px dotted gray;display:inline'>" +\
                k.date_publish.strftime('%Y-%m-%d') + "&emsp;" + k.user.username + '</p>' + "&emsp;"+ k.content + '</div>'
        html += create_childcomment_html(v, margin_left + 20)

    html += '</div>'
    return mark_safe(html)
