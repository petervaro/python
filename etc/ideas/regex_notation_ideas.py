#--- OPTION 1 -----------------------------------------------------------------#
#syntax:re
re.compile(r'<regex>')

#syntax:re
pattern = r'<regex>'

container = [
    #syntax:re
    r'<regex>',
    1, 2, 3
]

def wrapper(pattern):
    re.compile(pattern, GLOBAL_FLAGS)

wrapper(r'<regex>'#syntax:re
)

re.compile(r'<regex>'#syntax:re
)

re.compile(
    r'<regex>'#syntax:re
)

'{}.{}'.format()#syntax:fmt

'<html><head></head><body></body></html>'#syntax:html

'select * from book'#syntax:sql
'SELECT * FROM book'#syntax:sql

def function(pattern: '<regex>'= r'<regex>'#syntax:re
    ):
    pass

#--- OPTION 2 -----------------------------------------------------------------#
#syntax:re
re.compile(r'<regex>')
#end:re

r'<regex>'or':re'