from django import template
from ..models import Post,Category

def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#这个函数的功能是获取数据库中前 num 篇文章，这里 num 默认为 5


register = template.Library()
#实例化一个template.Library

@register.simple_tag
#这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了

def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag

def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')
"""
# 这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
# 且是 Python 的 date 对象，精确到月份，降序排列。接受的三个参数值表明了这些含义，
# 一个是 created_time ，即 Post 的创建时间，month 是精度，
# order='DESC' 表明降序排列（即离当前越近的时间越排在前面）
"""
@register.simple_tag

def get_categories():
    return Category.objects.all()

