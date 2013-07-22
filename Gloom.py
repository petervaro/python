#!/usr/bin/python3
# -*- coding: utf8 -*-

domain = [0.0, 1.0]
def hsba(h: [0, 360], s: domain, b: domain, a: domain = 1.) -> str:

    alpha = '' if a >= 1 else '{:02x}'.format(int(a*255))

    i = h // 60
    f = h / 60.0 - i
    p = b * (1.0 - s)
    q = b * (1.0 - f * s)
    t = b * (1.0 - (1.0 - f) * s)

    if i == 0:
        rgb = (b, t, p)
    elif i == 1:
        rgb = (q, b, p)
    elif i == 2:
        rgb = (p, b, t)
    elif i == 3:
        rgb = (p, q, b)
    elif i == 4:
        rgb = (t, p, b)
    elif i == 5:
        rgb = (b, p, q)

    return '#{:02X}{:02X}{:02X}{a}'.format(*[int(c*255) for c in rgb], a=alpha)

i  = 'italic'
b  = 'bold'
bg = 'background'
fg = 'foreground'
name  = 'name'
scope = 'scope'
prefs = 'settings'
font  = 'fontStyle'

NAME = 'Gloom'

style = {
    'author': 'Peter Varo (c)2013',
    'comment': 'Based on the Twilight theme of Michael Sheets',
    'uuid': '5E10F479-14B9-4DC1-B26C-557B2BB3FAE',
    name : NAME,
    prefs:
    [
        {
            prefs:
            {
                bg             : hsba(0, 0, .08),
                fg             : hsba(0, 0, .95),
                'caret'        : hsba(0, 0, .65),
                'invisibles'   : hsba(0, 0, 1, .10),
                'lineHighlight': hsba(0, 0, 1, .04),
                'selection'    : hsba(0, 0, 1, .08)
            }
        },
        {
            name  : 'Comment',
            scope : 'comment',
            prefs :
            {
                fg  : hsba(0, 0, .35),
                font: i
            }
        },
        {
            name : 'Constant',
            scope: 'constant',
            prefs:
            {
                fg: hsba(15, .65, .80)
            }
        },
        {
            name : 'Entity',
            scope: 'entity',
            prefs:
            {
                fg: hsba(30, .60, .60)
            }
        },
        {
            name : 'Keyword',
            scope: 'keyword',
            prefs:
            {
                fg: hsba(40, .50, .80)
            }
        },
        {
            name : 'Storage',
            scope: 'storage',
            prefs:
            {
                fg: hsba(50, .40, .95)
            }
        },
        {
            name : 'String',
            scope: 'string',
            prefs:
            {
                fg: hsba(75, .30, .60)
            }
        },
        {
            name : 'Support',
            scope: 'support',
            prefs:
            {
                fg: hsba(295, .15, .60)
            }
        },
        {
            name : 'Variable',
            scope: 'variable',
            prefs:
            {
                fg: hsba(220, .30, .65)
            }
        },
        {
            name : 'Invalid Deprecated',
            scope: 'invalid.deprecated',
            prefs:
            {
                bg: hsba(10, .25, .80, .25)
            }
        },
        {
            name : 'Invalid Illegal',
            scope: 'invalid.illegal',
            prefs:
            {
                bg: hsba(300, .50, .35, .60)
            }
        },


#-- DETAILS -------------------------------------------------------------------#
        {
            name : 'Entity Inherited Class',
            scope: 'entity.other.inherited-class',
            prefs:
            {
                fg: hsba(25, .70, .60),
                font: i
            }
        },
        {
            name : 'String Constant',
            scope: 'string constant',
            prefs:
            {
                fg: hsba(75, .30, .95)
            }
        },
        {
            name : 'String Interpolated',
            scope: 'string.interpolated',
            prefs:
            {
                fg: hsba(120, .10, .85)
            }
        },
        {
            name : 'Support Function',
            scope: 'support.function',
            prefs:
            {
                fg: hsba(55, .40, .85)
            }
        },
        {
            name : 'Constant Character Escape',
            scope: 'constant.character.escape',
            prefs:
            {
                fg: hsba(30, .75, .80)
            }
        },
        {
            name : 'Storage Modifier',
            scope: 'storage.modifier',
            prefs:
            {
                fg: hsba(30, .55, .80)
            }
        },


#-- LINTER --------------------------------------------------------------------#
        {
            name : 'SublimeLinter Annotations',
            scope: 'sublimelinter.annotations',
            prefs:
            {
                bg: '#FFFFAA',
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Error Outline',
            scope: 'sublimelinter.outline.illegal',
            prefs:
            {
                bg: hsba(20, .80, .60),
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Error Underline',
            scope: 'sublimelinter.underline.illegal',
            prefs:
            {
                bg: hsba(20, .80, .95)
            }
        },
        {
            name : 'SublimeLinter Warning Outline',
            scope: 'sublimelinter.outline.warning',
            prefs:
            {
                bg: hsba(40, .50, .50),
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Warning Underline',
            scope: 'sublimelinter.underline.warning',
            prefs:
            {
                bg: hsba(40, .50, .85)
            }
        },
        {
            name : 'SublimeLinter Violation Outline',
            scope: 'sublimelinter.outline.violation',
            prefs:
            {
                bg: hsba(75, .40, .35),
                fg: hsba(0, 0, 1)
            }
        },
        {
            name : 'SublimeLinter Violation Underline',
            scope: 'sublimelinter.underline.violation',
            prefs:
            {
                bg: hsba(75, .40, .70)
            }
        }
    ]
}

if __name__ == '__main__':
    import convert
    convert.dict_to_theme(
        dictionary = style,
        name  = NAME,
        path  = '~/Library/Application Support/Sublime Text 3/Packages/Color Scheme - Default/',
        local = True
    )
    with open('{}.css'.format(NAME), 'w') as f:
        f.write(convert.dict_to_css(style, NAME))
