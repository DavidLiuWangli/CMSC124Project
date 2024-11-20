GRAMMARS = {
    'program': [
        ['outsides', 'HAI', 'end-of-line', 'data-section', 'statements', 'KTHXBYE', 'end-of-line', 'outsides']
    ],
    'outsides': [
        ['outside', 'outsides'],
        ['']
    ],
    'outside': [
        ['function'],
        ['comment'],
        ['multi-line-comment']
    ],
    'statements': [
        ['statement', 'statements'],
        ['']
    ],
    'statement': [
        ['comment'],
        ['multi-line-comment'],
        ['input'],
        ['output'],
        ['expression', 'end-of-line'],
        ['variable-assignment'],
        ['condition-block'],
        ['switch-case block'],
        ['loop block'],
        ['function-call']
    ],
    'comment': [
        ['BTW', 'comtext', 'linebreak']
    ],
    'multi-line-comment': [
        ['OBTW', 'comtext', 'linebreak', 'multi-content', 'comtext', 'TLDR', 'end-of-line']
    ],
    'multi-content': [
        ['comtext', 'linebreak', 'multi-content'],
        ['']
    ],
    'data-section': [
        ['WAZZUP', 'end-of-line', 'declarations', 'BUHBYE', 'end-of-line'],
        ['']
    ],
    'declarations': [
        ['I HAS A', 'varident', 'initialization', 'end-of-line', 'declarations'],
        ['end-of-line', 'declarations'],
        ['']
    ],
    'initialization': [
        ['ITZ', 'value'],
        ['']
    ],
    'value': [
        ['literal'],
        ['expression'],
        ['varident']
    ],
    'literal': [
        ['numbr'],
        ['numbar'],
        ['yarn'],
        ['troof']
    ],
    'expression': [
        ['math-expression'],
        ['concatenation'],
        ['boolean-expression'],
        ['comparison-expression'],
        ['all-any-expression'],
        ['typecasting']
    ],
    'input': [
        ['GIMMEH', 'varident', 'end-of-line']
    ],
    'output': [
        ['VISIBLE', 'operand', 'output-operands', 'end-of-line']
    ],
    'output-operands': [
        ['+', 'operand', 'output-operands'],
        ['']
    ],
    'operand': [
        ['varident'],
        ['literal'],
        ['IT'],
        ['expression']
    ],
    'math-expression': [
        ['math-operator', 'operand', 'AN', 'operand']
    ],
    'math-operator': [
        ['SUM OF'],
        ['DIFF OF'],
        ['PRODUKT OF'],
        ['QUOSHUNT OF'],
        ['MOD OF']
    ],
    'concatenation': [
        ['SMOOSH', 'operand', 'concatenation-operands']
    ],
    'concatenation-operands': [
        ['AN', 'operand', 'concatenation-operands'],
        ['']
    ],
    'boolean-expression': [
        ['boolean-operator', 'operand', 'AN', 'operand'],
        ['NOT', 'operand']
    ],
    'boolean-operator': [
        ['BOTH OF'],
        ['EITHER OF'],
        ['WON OF']
    ],
    'comparison-expression': [
        ['comparison-operator', 'operand', 'AN', 'operand']
    ],
    'comparison-operator': [
        ['BOTH SAEM'],
        ['DIFFRINT'],
        ['BIGGR OF'],
        ['SMALLR OF']
    ],
    'inequality': [
        ['BIGGR OF', 'operand', 'AN'],
        ['SMALLR OF', 'operand', 'AN'],
        ['']
    ],
    'all-any-expression': [
        ['all-any-operator', 'all-any-operand', 'all-any-operands', 'MKAY']
    ],
    'all-any-operator': [
        ['ALL OF'],
        ['ANY OF']
    ],
    'all-any-operands': [
        ['AN', 'all-any-operand', 'all-any-operands'],
        ['all-any-operand']
    ],
    'all-any-operand': [
        ['varident'],
        ['literal'],
        ['IT'],
        ['all-any-math'],
        ['all-any-boolean'],
        ['all-any-concatenation'],
        ['all-any-comparison']
    ],
    'all-any-math': [
        ['math-operator', 'all-any-operand', 'AN', 'all-any-operand']
    ],
    'all-any-boolean': [
        ['boolean-operator', 'all-any-operand', 'AN', 'all-any-operand'],
        ['NOT', 'all-any-operand']
    ],
    'all-any-concatenation': [
        ['SMOOSH', 'all-any-operand', 'all-any-concatenation-operands']
    ],
    'all-any-concatenation-operands': [
        ['AN', 'all-any-operand', 'all-any-concatenation-operands'],
        ['']
    ],
    'all-any-comparison': [
        ['comparison-operator', 'all-any-operand', 'AN', 'inequality', 'all-any-operand']
    ],
    'typecasting': [
        ['MAEK', 'varident', 'typecasting-separator', 'type'],
    ],
    'typecasting-separator': [
        ['A'],
        ['']
    ],
    're-casting': [
        ['varident', 'IS NOW A', 'type', 'end-of-line']
    ],
    'variable-assignment': [
        ['variable-reference', 'R', 'value'],
    ],
    'variable-reference': [
        ['varident'],
        ['IT']
    ],
    'control-body': [
        ['statement'],
        ['GTFO']
    ],
    'condition-block': [
        ['expression', 'end-of-line', 'O RLY?', 'end-of-line', 'YA RLY', 'end-of-line', 'statement', 'else-if-chain', 'else-block', 'end-of-line', 'OIC', 'end-of-line']
    ],
    'else-if-chain': [
        ['else-if-block', 'else-if-chain'],
        ['']
    ],
    'else-if-block': [
        ['MEBBE', 'expression', 'end-of-line', 'statement', 'end-of-line']
    ],
    'else-block': [
        ['NO WAI', 'end-of-line', 'statement', 'end-of-line'],
        ['']
    ],
    'switch-case block': [
        ['varident', ',', 'WTF?', 'end-of-line', 'cases-chain', 'default-case-block', 'OIC'],
        ['WTF?', 'end-of-line', 'cases-chain', 'default-case-block', 'OIC', 'end-of-line']
    ],
    'cases-chain': [
        ['case-block', 'cases-chain'],
        ['']
    ],
    'case-block': [
        ['OMG', 'literal', 'end-of-line', 'control-body', 'end-of-line']
    ],
    'default-case-block': [
        ['OMGWTF', 'literal', 'end-of-line', 'control-body', 'end-of-line'],
        ['']
    ],
    'loop-block': [
        ['IM IN YR', 'loopident', 'loop-direction', 'YR', 'varident', 'loop-condition', 'end-of-line', 'control-body', 'end-of-line', 'IM OUTTA YR', 'loopident', 'end-of-line']
    ],
    'loop-direction': [
        ['UPPIN'],
        ['NERFIN']
    ],
    'loop-condition': [
        ['TIL', 'expression'],
        ['WILE', 'expression']
    ],
    'function': [
        ['HOW IZ I', 'funcident', 'parameters', 'end-of-line', 'function-body', 'IF U SAY SO', 'end-of-line']
    ],
    'function-call': [
        ['I IZ', 'funcident', 'arguments', 'MKAY', 'end-of-line']
    ],
    'parameters': [
        ['YR', 'varident', 'extra-parameters'],
        ['']
    ],
    'extra-parameters': [
        ['AN', 'YR', 'varident', 'extra-parameters'],
        ['']
    ],
    'arguments': [
        ['YR', 'value', 'extra-arguments'],
        ['']
    ],
    'extra-arguments': [
        ['AN', 'YR', 'value', 'extra-arguments'],
        ['']
    ],
    'return': [
        ['FOUND YR', 'value'],
        ['GTFO']
    ],
    'function-body': [
        ['statement', 'function-body'],
        ['']
    ],
    'end-of-line': [
        ['comment'],
        ['linebreak']
    ],
    'comtext': [
        ['text'],
        ['']
    ],
    'funcident': [
        ['varident']
    ],
    'loopident': [
        ['varident']
    ]
}
