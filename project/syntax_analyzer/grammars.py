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
        ['re-casting'],
        ['variable-assignment'],
        ['condition-block'],
        ['switch-case block'],
        ['loop-block'],
        ['function-call'],
        ['function']
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
        ['GIMMEH', 'variable-reference', 'end-of-line']
    ],
    'output': [
        ['VISIBLE', 'operand', 'output-operands', 'end-of-line']
    ],
    'output-operands': [
        ['+', 'operand', 'output-operands'],
        ['AN', 'operand', 'output-operands'],
        ['operand', 'output-operands'],
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
        ['']
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
        ['variable-reference', 'R', 'value', 'end-of-line'],
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
        ['expression', 'end-of-line', 'O RLY?', 'end-of-line', 'YA RLY', 'end-of-line', 'statements', 'else-if-chain', 'else-block', 'OIC', 'end-of-line']
    ],
    'else-if-chain': [
        ['else-if-block', 'else-if-chain'],
        ['']
    ],
    'else-if-block': [
        ['MEBBE', 'expression', 'end-of-line', 'statements']
    ],
    'else-block': [
        ['NO WAI', 'end-of-line', 'statements'],
        ['']
    ],
    'switch-case block': [
        ['varident', 'end-of-line', 'WTF?', 'end-of-line', 'cases-chain', 'default-case-block', 'OIC', 'end-of-line'],
        ['WTF?', 'end-of-line', 'cases-chain', 'default-case-block', 'OIC', 'end-of-line']
    ],
    'cases-chain': [
        ['case-block', 'cases-chain'],
        ['']
    ],
    'case-block': [
        ['OMG', 'literal', 'end-of-line', 'control-body']
    ],
    'default-case-block': [
        ['OMGWTF', 'end-of-line', 'control-body'],
        ['']
    ],
    'control-body': [
        ['GTFO', 'end-of-line'],
        ['statement', 'control-body'],
        ['']
    ],
    'loop-block': [
        ['IM IN YR', 'loopident', 'loop-direction', 'YR', 'varident', 'loop-condition', 'end-of-line', 'control-body', 'IM OUTTA YR', 'loopident', 'end-of-line']
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
        ['FOUND YR', 'value', 'end-of-line'],
        ['GTFO', 'end-of-line']
    ],
    'function-body': [
        ['statement', 'function-body'],
        ['return', 'function-body'],
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
