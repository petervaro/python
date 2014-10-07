## INFO ########################################################################
##                                                                            ##
##                   Python and Cython Syntax Highlighters                    ##
##                   =====================================                    ##
##                                                                            ##
##                       Version: 2.0.00.053 (20141007)                       ##
##                             File: src/utils.py                             ##
##                                                                            ##
##            For more information about the project, please visit            ##
##                   <https://github.com/petervaro/python>.                   ##
##                    Copyright (C) 2013 - 2014 Peter Varo                    ##
##                                                                            ##
##  This program is free software: you can redistribute it and/or modify it   ##
##   under the terms of the GNU General Public License as published by the    ##
##       Free Software Foundation, either version 3 of the License, or        ##
##                    (at your option) any later version.                     ##
##                                                                            ##
##    This program is distributed in the hope that it will be useful, but     ##
##         WITHOUT ANY WARRANTY; without even the implied warranty of         ##
##            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.            ##
##            See the GNU General Public License for more details.            ##
##                                                                            ##
##     You should have received a copy of the GNU General Public License      ##
##     along with this program, most likely a file in the root directory,     ##
##        called 'LICENSE'. If not, see <http://www.gnu.org/licenses>.        ##
##                                                                            ##
######################################################################## INFO ##


#------------------------------------------------------------------------------#
# HSBA Color Object
class hsba:

    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def __init__(self, hue        : '0 .. 360',
                       saturation : '0.0 .. 1.0',
                       brightness : '0.0 .. 1.0',
                       alpha      : '0.0 .. 1.0' = 1.0):
        # Store static values
        self._hue = hue
        self._saturation = saturation
        self._brightness = brightness
        self._alpha = alpha

        # Convert and store RGBA values too
        self._to_rgba()


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def _to_rgba(self):
        # Get local references
        h = self._hue
        s = self._saturation
        b = self._brightness
        a = self._alpha

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

        # Store converted values
        self._rgba = rgb + (a,)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def to_hex(self):
        # Convert to hexadecimal string representation
        alpha = '' if self._alpha >= 1.0 else '{:02X}'.format(int(self._alpha*255))
        return '#{:02X}{:02X}{:02X}{a}'.format(*(int(c*255) for c in self._rgba[:3]), a=alpha)


    #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def to_rgba(self):
        # Convert to CSS's rgba() string representation
        return 'rgba({}, {}, {}, {:.2f})'.format(*self._rgba)



#------------------------------------------------------------------------------#
# Generate section captions
def separator(*captions):
    for caption in captions:
        print('#{:-<78}#'.format('-- {} '.format(caption.upper())))
