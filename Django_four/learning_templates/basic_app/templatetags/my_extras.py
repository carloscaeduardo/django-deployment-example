# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    Parameters
    ----------
    value : str
    arg : str

    This cuts out all cvalues of "arg" from the value.
    -------
    PRE-condition: value must be a string.
    
    >>>cut("Hello World", "World")
    "Hello "
    """
    
    return value.replace(arg,'')


# register.filter('cut' ,cut)