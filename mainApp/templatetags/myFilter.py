from django import template
register = template.Library()


@register.filter(name = 'solution_num_to_alpha')
def solution_num_to_alpha(value):
    return chr(value + 64)
