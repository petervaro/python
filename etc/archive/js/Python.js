/*
 * Python 3 Regular Expressions
 *
 * @author Peter Varo
 * @version 2.0.0
 */

var self = [
//- COMMENT ------------------------------------------------------------------//
    {
        'name' : 'comment.line.hashmark.python',
        'pattern': /#.*/g
    },


//- LAMBDA -------------------------------------------------------------------//
    {
        'pattern': /\b(lambda)(\s+(\*{0,2}[A-z_]\w*\s*(,|=.+(?=,|:))?\s*)*)?(?=:)/g,
        'matches':
        {
            1: 'storage.type.function.anonymous.python',
            2:
            {
                'pattern': /\*{0,2}([A-z_]\w*)\s*(,|=.+(?=,|:))?\s*/g,
                'matches':
                {
                    1: 'variable.parameter.function.python',
                    2:
                    {
                        'pattern': /(=)(.+)(?=,|:)/g,
                        'matches':
                        {
                            1: 'keyword.operator.assignment.python',
                            2:
                            {
                                'language': 'python'
                            }
                        }
                    }
                }
            }
        }
    },


//- NUMBERS ------------------------------------------------------------------//
    {
        'name' : 'constant.numeric.integer.binary.python',
        'pattern': /\b0b[01]+/g
    },
    {
        'name' : 'constant.numeric.integer.hexadecimal.python',
        'pattern': /\b0x[0-9a-fA-F]+/g
    },
    {
        'name' : 'constant.numeric.integer.octal.python',
        'pattern': /\b0o[0-7]+/g
    },
    {
        //.001  .1e6  .1E6  .1e+6  .1E+6  .1e-6  .1E-6
        'name' : 'constant.numeric.float_and_complex.decimal.floatnumber.python',
        'pattern': /(?=\W)\.\d+([eE][+-]?\d+)?[jJ]?/g
    },
    {
        //1.  1.0  1.1e6  1.1E6  1.1e+6  1.1E+6  1.1e-6  1.1E-6
        'name' : 'constant.numeric.float_and_complex.decimal.pointfloat.python',
        'pattern': /\d+\.(\d+([eE][+-]?\d+)?)?[jJ]?/g
    },
    {
        //1e6  1E6  1e+6  1E+6  1e-6  1E-6
        'name' : 'constant.numeric.float_and_complex.decimal.exponent.python',
        'pattern': /\b(?!\.)\d+[eE][+-]?\d+[jJ]?/g
    },
    {
        'name' : 'constant.numeric.integer_and_complex.decimal.python',
        'pattern': /\b(?!\.)([1-9]\d*|0)[jJ]?/g
    },


//- KEYWORDS -----------------------------------------------------------------//
    {
        'name' : 'storage.modifier.declaration.python',
        'pattern': /\b(global|nonlocal)\b/g
    },
    {
        'name' : 'keyword.control.import_and_import_from.python',
        'pattern': /\b(import|from)\b/g
    },
    {
        'name' : 'keyword.control.flow_block_delimiters.python',
        'pattern': /\b(elif|else|except|finally|for|if|try|while|with|break|continue|pass|raise|return|yield)\b/g
    },
    {
        'name' : 'keyword.operator.bool.logical.python',
        'pattern': /\b(and|in|is|not|or)\b/g
    },
    {
        'name' : 'keyword.other.python',
        'pattern': /\b(as|assert|del)\b/g
    },


//- OPERATORS ----------------------------------------------------------------//
    {
        'name' : 'keyword.operator.comparison.python',
        'pattern': /&lt;=|&gt;=|==|&lt;|&gt;|!=/g
    },
    {
        'name' : 'keyword.operator.assignment.augmented.python',
        'pattern': /\+=|-=|\*=|\/=|\/\/=|%=|&amp;=|\|=|\^=|&lt;&lt;=|&gt;&gt;=|\*\*=/g
    },
    {
        'name' : 'keyword.operator.arithmetic.python',
        'pattern': /\+|-|\*|\*\*|\/|\/\/|%|&lt;&lt;|&gt;&gt;|&amp;|\||\^|~/g
    },
    {
        'name' : 'keyword.operator.value_and_annotation_assignment.python',
        'pattern': /=|-&gt;/g
    },


//- CLASS --------------------------------------------------------------------//
    {
        'pattern': /\s*(class)\s+([A-z_]\w*)(\s*\((([A-z_]\w*\s*,?\s*)|([A-z_]\w*\s*=\s*[A-z_]\w*))*\))?:/g,
        'matches':
        {
            1: 'storage.type.class.python',
            2: 'entity.name.type.class.python',
            3:
            {
                'pattern': /([A-z_]\w*\s*,?\s*)|([A-z_]\w*\s*=\s*[A-z_]\w*)/g,
                'matches':
                {
                    1:
                    {
                        'pattern': /([A-z_]\w*)\s*,?\s*/g,
                        'matches':
                        {
                            //todo: invalid.illegal names (reserved keywords)
                            1: 'entity.other.inherited-class.python'
                        }
                    },
                    2:
                    {
                        'pattern': /([A-z_]\w*)\s*(=)\s*([A-z_]\w*)/g,
                        'matches':
                        {
                            1: 'entity.other.inherited-class.python',
                            2: 'keyword.operator.assignment.python',
                            3: 'entity.other.inherited-class.python'
                        }
                    }
                }
            }
        }
    },


//- FUNCTION -----------------------------------------------------------------//
    {
        //'pattern': /\s*(def)\s+([A-z_]\w*)\s*\((([A-z_]\w*\s*(?=,|[\n)])\s*)*(\*[A-z_]\w*\s*(?=,|[\n)])\s*)?([A-z_]\w*\s*=\s*.+(?=,|[\n)])\s*)*(\*\*[A-z_]\w*(?=[\n)])\s*)?)\):/g,
        'pattern': /\s*(def)\s+([A-z_]\w*)\s*\((\*?\*?([A-z_]\w*)\s*(:.+(?=,|=|[\n)]))?\s*(=.+(?=,|[\n)]))?\s*)*\)\s*(-&gt;.+)?(?=:)/g,
        'matches':
        {
            1: 'storage.type.function.python',
            2: 'entity.name.function.python',
            3:
            {
                'pattern': /\*?\*?([A-z_]\w*)\s*(?=:.+(?=,|=|[\n)]))?\s*(?==.+(?=,|[\n)]))?\s*/g,
                'matches':
                {
                    1: 'variable.parameter.function.python'
                }
            },
            4:
            {
                'pattern': /(-&gt;).+/g,
                'matches':
                {
                    1: 'keyword.operator.assignment.python'
                }
            }
            // 3:
            // {
            //     'pattern': /([A-z_]\w*\s*(?=,|[\n)])\s*)*(\*[A-z_]\w*\s*(?=,|[\n)])\s*)?([A-z_]\w*\s*=\s*.+(?=,|[\n)])\s*)*(\*\*[A-z_]\w*(?=[\n)])\s*)?/g,
            //     'matches':
            //     {
            //         1:
            //         {
            //             'pattern': /([A-z_]\w*)\s*(?=,|[\n)])\s*/g,
            //             'matches':
            //             {
            //                 1: 'variable.parameter.function.python',
            //                 3: /(\*{0,2}([A-z_]\w*)\s*(:.+(?=,|=|[\n)]))?\s*(=.+(?=,|[\n)]))?)*/
            //             }
            //         },
            //         2:
            //         {
            //             'pattern': /\*([A-z_]\w*)\s*(?=,|[\n)])\s*/g,
            //             'matches':
            //             {
            //                 1: 'variable.parameter.function.python'
            //             }
            //         },
            //         3:
            //         {
            //             'pattern': /([A-z_]\w*)\s*=\s*.+(?=,|[\n)])\s*/g,
            //             'matches':
            //             {
            //                 1: 'variable.parameter.function.python',
            //                 2: 'keyword.operator.assignment.python'
            //             }
            //         },
            //         4:
            //         {
            //             'pattern': /\*\*([A-z_]\w*)(?=[\n)])\s*/g,
            //             'matches':
            //             {
            //                 1: 'variable.parameter.function.python'
            //             }
            //         }
            //     }
            // }
        }
    }
];

Rainbow.extend('python', self, true);
