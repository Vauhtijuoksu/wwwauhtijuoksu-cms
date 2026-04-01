# autogen default and fullscreen for year...
yearly_templates = ["26", "25+", "25", "24", "23", "22", "21+"]
generic = [
    ('vauhtijuoksu/main/generic/default.html', 'VJ SideViuhti (Generic)'),
    ('vauhtijuoksu/main/generic/fullscreen.html', 'VJ SideViuhti Fullscreen (Generic)'),
    ('vauhtijuoksu/main/generic/doc.html', 'Document'),
]
additional = [
    ('vauhtijuoksu/main/vj21/default.html', 'VJ 2021 theme'),
    ('vauhtijuoksu/main/deprecated/genericViolet.html', 'VJ OLD Generic violet theme'),
]

# List of templates that can be used for CMS pages
def vauhtijuoksu_templates():
    templates = []
    for t in generic:
        templates.append(t)

    for y in yearly_templates:
        templates.append((f'vauhtijuoksu/main/{"vj" + y.replace("+", "plus")}/default.html', "VJ" + y + " theme default"))
        templates.append((f'vauhtijuoksu/main/{"vj" + y.replace("+", "plus")}/fullscreen.html', "VJ" + y + " theme fullscreen"))

    for t in additional:
        templates.append(t)
    return templates

