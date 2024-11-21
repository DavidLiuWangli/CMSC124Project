import re

REGEX_TOKENS = {
    # Separators
    'I/0 Seperator': r'^\+$',
    'Identifier Seperator': r'^AN$', 
    
    # Comments
    'Comment': r'^BTW\s.*$',
    'Multiline Comment Start': r'^OBTW$',
    'Multiline Comment End': r'^TLDR$',
    
    # Keywords
    'Program Start': r'^HAI$',
    'Program End': r'^KTHXBYE$',
    'Data Section Start': r'^WAZZUP$',
    'Data Section End': r'^BUHBYE$',
    'Variable Declaration': r'^I HAS A$',
    'Variable Initialize': r'^ITZ$',
    'Assigment Operator': r'^R$',
    
    # Arithmetic operations
    'Sum Operator': r'^SUM OF$',
    'Difference Operator': r'^DIFF OF$',
    'Product Operator': r'^PRODUKT OF$',
    'Quotient Operator': r'^QUOSHUNT OF$',
    'Modulus Operator': r'^MOD OF$',
    'Greater Operator': r'^BIGGR OF$',
    'Smaller Operator': r'^SMALLR OF$',

    # Boolean operations
    'And Operator': r'^BOTH OF$',
    'Or Operator': r'^EITHER OF$',
    'Xor Operator': r'^WON OF$',
    'Not Operator': r'^NOT$',

    # Any/All expressions
    'Any Operator': r'^ANY OF$',
    'All Operator': r'^ALL OF$',

    # Comparison
    'Equality Operator': r'^BOTH SAEM$',
    'Inequality Operator': r'^DIFFRINT$',

    # Concatenation
    'Concatenator': r'^SMOOSH$',

    # Typecasting
    'Output Typecast': r'^MAEK$',
    'Typecast Result': r'^A$',
    'Self Typecast': r'^IS NOW A$',

    # Input/Output
    'Console Output': r'^VISIBLE$',
    'Console Input': r'^GIMMEH$',

    # Conditionals
    'If Keyword': r'^O RLY\?$',
    'If True Keyword': r'^YA RLY$',
    'If Else Keyword': r'^MEBBE$',
    'If False Keyword': r'^NO WAI$',
    'If End Keyword': r'^OIC$',

    # Switch-case
    'Switch Keyword': r'^WTF\?$',
    'Case Keyword': r'^OMG$',
    'Default Case Keyword': r'^OMGWTF$',
    'Break Keyword': r'^GTFO$',

    # Loops
    'Loop Keyword': r'^IM IN YR$',
    'Loop Increment': r'^UPPIN$',
    'Loop Decrement': r'^NERFIN$',
    'Loop Variable': r'^YR$',
    'Loop Until Condition': r'^TIL$',
    'Loop While Condition': r'^WILE$',
    'Loop End Keyword': r'^IM OUTTA YR$',

    # Functions
    'Function Declaration': r'^HOW IZ I$',
    'Function End': r'^IF U SAY SO$',
    'Function Call': r'^I IZ$',
    'Function Return': r'^FOUND YR$',
    'Exit': r'^GTFO$',
    
    # Miscellaneous
    'Identifiers End Keyword': r'^MKAY$',

    # Literals
    'Integer Literal': r'^(\-?(0+)|\-?[1-9][0-9]*)$',
    'Number Literal': r'^\-?[0-9]+\.[0-9]+$',
    'String Literal': r'^\"[^\"]*\"$',
    'Boolean Literal': r'^(WIN|FAIL)$',
    'Type Literal': r'^(NUMBR|NUMBAR|YARN|TROOF|NOOB)$',

    # Identifiers
    'Variable Identifier': r'^[A-Za-z][A-Za-z0-9_]*$',
    'Function Identifier': r'^[A-Za-z][A-Za-z0-9_]*$',
    'Loop Identifier': r'^[A-Za-z][A-Za-z0-9_]*$',
}
