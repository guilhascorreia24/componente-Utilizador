from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
    try:
        result = field.as_widget(attrs={"class":css})
        return result
    except:
        print(field)

