from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg

@register.filter(name='divisible')
def divisible(value, arg):
    return int(value / arg)
