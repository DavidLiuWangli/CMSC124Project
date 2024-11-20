GRAMMARS = {
    'program': [
        ['outside', 'linebreak', 'program'],
        ['program', 'linebreak', 'outside'],
        ['HAI', 'content', 'KTHXBYE'],
        ['HAI', 'comment', 'content', 'KTHXBYE'],
        ['HAI', 'content', 'KTHXBYE', 'comment'],
        ['HAI', 'comment', 'content', 'KTHXBYE', 'comment']
    ],
    'outside': [
        ['outside', 'linebreak', 'outside'],
        ['function'],
        ['comment'],
        ['multi-line comment']
    ],
    'content': [
        ['linebreak', 'data section', 'main'],
        ['main']
    ],
    'main': [
        ['linebreak', 'statement', 'end-of-line']
    ],
    'statement': [
        ['general-statement', 'end-of-line', 'statement'],
        ['general-statement']
    ],
    'general-statement': [
        ['comment'],
        ['multi-line comment'],
        ['input'],
        ['output'],
        ['expression'],
        ['variable-assignment'],
        ['condition-block'],
        ['switch-case block'],
        ['loop block'],
        ['function-call']
    ],
    'comment': [
        ['BTW', 'comtext']
    ],
    'multi-line comment': [
        ['OBTW', 'linebreak', 'multi-content', 'linebreak', 'TLDR'],
        ['OBTW', 'comtext', 'linebreak', 'multi-content', 'linebreak', 'TLDR'],
        ['OBTW', 'linebreak', 'multi-content', 'linebreak', 'comtext', 'TLDR'],
        ['OBTW', 'comtext', 'linebreak', 'multi-content', 'linebreak', 'comtext', 'TLDR']
    ],
    'multi-content': [
        ['comtext', 'linebreak', 'multi-content'],
        ['comtext']
    ],
    'data section': [
        ['WAZZUP', 'declarations', 'BUHBYE'],
        ['WAZZUP', 'comments', 'declarations', 'BUHBYE'],
        ['WAZZUP', 'declarations', 'BUHBYE', 'comment'],
        ['WAZZUP', 'comments', 'declarations', 'BUHBYE', 'comment']
    ],
    'declarations': [
        ['linebreak', 'declaration', 'linebreak']
    ],
    'declaration': [
        ['declaration', 'end-of-line', 'declaration'],
        ['I HAS A', 'varident'],
        ['I HAS A', 'varident', 'ITZ', 'literal'],
        ['I HAS A', 'varident', 'ITZ', 'varident'],
        ['I HAS A', 'varident', 'ITZ', 'expression']
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
        ['GIMMEH', 'varident']
    ],
    'output': [
        ['VISIBLE', 'output operands']
    ],
    'output operands': [
        ['operand', '+', 'output operands'],
        ['operand']
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
        ['QUOSHUNT'],
        ['MOD OF']
    ],
    'concatenation': [
        ['SMOOSH', 'concatenation operands']
    ],
    'concatenation operands': [
        ['operand', 'AN', 'concatenation operands'],
        ['operand']
    ],
    'boolean-expression': [
        ['boolean-operator', 'operand', 'AN', 'operand'],
        ['not', 'operand']
    ],
    'boolean-operator': [
        ['BOTH OF'],
        ['EITHER OF'],
        ['WON OF']
    ],
    'not': [
        ['NOT']
    ],
    'comparison-expression': [
        ['comparison-operator', 'operand', 'AN', 'operand'],
        ['comparison-operator', 'operand', 'AN', 'inequality', 'AN', 'operand']
    ],
    'comparison-operator': [
        ['BOTH SAEM'],
        ['DIFFRINT']
    ],
    'inequality': [
        ['BIGGR OF'],
        ['SMALLR OF']
    ],
    'all-any-expression': [
        ['all-any-operator', 'all-any-operands', 'MKAY']
    ],
    'all-any-operator': [
        ['ALL OF'],
        ['ANY OF']
    ],
    'all-any-operands': [
        ['all-any-operand', 'AN', 'all-any-operands'],
        ['all-any-operand']
    ],
    'typecasting': [
        ['MAEK', 'varident', 'A', 'type'],
        ['MAEK', 'varident', 'type']
    ],
    're-casting': [
        ['varident', 'IS NOW A', 'type']
    ],
    'variable-assignment': [
        ['variable-reference', 'R', 'literal'],
        ['variable-reference', 'R', 'variable-reference'],
        ['variable-reference', 'R', 'expression']
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
        ['expression', 'end-of-line', 'O RLY?', 'end-of-line', 'YA RLY', 'end-of-line', 'statement', 'end-of-line', 'OIC', 'end-of-line'],
        ['expression', 'end-of-line', 'O RLY?', 'end-of-line', 'YA RLY', 'end-of-line', 'statement', 'then block', 'end-of-line', 'OIC', 'end-of-line']
    ],
    'then block': [
        ['else-if chain', 'else block'],
        ['else block'],
        ['else-if chain']
    ],
    'else-if chain': [
        ['else-if block', 'else-if chain'],
        ['else-if block']
    ],
    'else-if block': [
        ['MEBBE', 'expression', 'end-of-line', 'statement', 'end-of-line']
    ],
    'else block': [
        ['NO WAI', 'end-of-line', 'statement', 'end-of-line']
    ],
    'switch-case block': [
        ['varident', ',', 'WTF?', 'end-of-line', 'cases-chain', 'OIC'],
        ['WTF?', 'end-of-line', 'cases-chain', 'OIC', 'end-of-line']
    ],
    'cases-chain': [
        ['case-block', 'cases-chain'],
        ['case-block'],
        ['default-case-block']
    ],
    'case-block': [
        ['OMG', 'literal', 'end-of-line', 'control-body', 'end-of-line']
    ],
    'default-case-block': [
        ['OMGWTF', 'literal', 'end-of-line', 'control-body', 'end-of-line']
    ],
    'loop block': [
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
        ['HOW IZ I', 'funcident', 'parameters', 'end-of-line', 'function-body', 'IF U SAY SO']
    ],
    'function-call': [
        ['I IZ', 'funcident', 'arguments', 'MKAY', 'end-of-line']
    ],
    'parameters': [
        ['YR', 'varident'],
        ['YR', 'varident', 'AN', 'arguments'],
    ],
    'arguments': [
        ['YR', 'expression'],
        ['YR', 'expression', 'AN', 'parameters'],
    ],
    'return': [
        ['FOUND YR', 'varident'],
        ['FOUND YR', 'expression'],
        ['GTFO']
    ],
    'function-body': [
        ['statement', 'end-of-line', 'function-body'],
        ['return', 'end-of-line', 'function-body'],
        ['statement', 'end-of-line'],
        ['return', 'end-of-line']
    ]
}
