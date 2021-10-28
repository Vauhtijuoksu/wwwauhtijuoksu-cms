from django import template

register = template.Library()

@register.filter(name='duration')
def render_duration(value):
    # Renders a time estimate given in seconds
    value = int(value)
    hours = value // 3600
    minutes = (value % 3600) // 60
    seconds = (value % 60)

    s = ''
    if hours:
        s += f' {hours}h'
    if minutes:
        s += f' {minutes}min'
    if seconds:
        s += f' {seconds}sec'

    return s.strip()

@register.filter(name='split')
def split(value, key):
  return value.split(key)

@register.filter(name='zip')
def zip_lists(a, b):
  return zip(a, b)

@register.filter(name='toint')
def to_int(s):
  return int(s)

@register.filter(name='percentof')
def percent_of(a,b):
  return float(a)/float(b)*100

@register.filter(name='fiweekday')
def weekday_fi(daynumber):
    fiweekdays = ["Sunnuntai", "Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai"]
    return fiweekdays[int(daynumber)]