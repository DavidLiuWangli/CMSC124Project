import re

REGEX_TOKENS = {
    # Separators
    '+': r'^\+$',
    'AN': r'^AN$', 
    
    # Comments
    'BTW': r'^BTW\s.*$',
    'OBTW': r'^OBTW$',
    'TLDR': r'^TLDR$',
    
    # Keywords
    'HAI': r'^HAI$',
    'KTHXBYE': r'^KTHXBYE$',
    'WAZZUP': r'^WAZZUP$',
    'BUHBYE': r'^BUHBYE$',
    'I HAS A': r'^I HAS A$',
    'ITZ': r'^ITZ$',
    'R': r'^R$',
    
    # Arithmetic operations
    'SUM OF': r'^SUM OF$',
    'DIFF OF': r'^DIFF OF$',
    'PRODUKT OF': r'^PRODUKT OF$',
    'QUOSHUNT OF': r'^QUOSHUNT OF$',
    'MOD OF': r'^MOD OF$',
    'BIGGR OF': r'^BIGGR OF$',
    'SMALLR OF': r'^SMALLR OF$',

    # Boolean operations
    'BOTH OF': r'^BOTH OF$',
    'EITHER OF': r'^EITHER OF$',
    'WON OF': r'^WON OF$',
    'NOT': r'^NOT$',

    # Any/All expressions
    'ANY OF': r'^ANY OF$',
    'ALL OF': r'^ALL OF$',

    # Comparison
    'BOTH SAEM': r'^BOTH SAEM$',
    'DIFFRINT': r'^DIFFRINT$',

    # Concatenation
    'SMOOSH': r'^SMOOSH$',

    # Typecasting
    'MAEK': r'^MAEK$',
    'A': r'^A$',
    'IS NOW A': r'^IS NOW A$',

    # Input/Output
    'VISIBLE': r'^VISIBLE$',
    'GIMMEH': r'^GIMMEH$',

    # Conditionals
    'O RLY?': r'^O RLY\?$',
    'YA RLY': r'^YA RLY$',
    'MEBBE': r'^MEBBE$',
    'NO WAI': r'^NO WAI$',
    'OIC': r'^OIC$',

    # Switch-case
    'WTF?': r'^WTF\?$',
    'OMG': r'^OMG$',
    'OMGWTF': r'^OMGWTF$',
    'GTFO': r'^GTFO$',

    # Loops
    'IM IN YR': r'^IM IN YR$',
    'UPPIN': r'^UPPIN$',
    'NERFIN': r'^NERFIN$',
    'YR': r'^YR$',
    'TIL': r'^TIL$',
    'WILE': r'^WILE$',
    'IM OUTTA YR': r'^IM OUTTA YR$',

    # Functions
    'HOW IZ I': r'^HOW IZ I$',
    'IF U SAY SO': r'^IF U SAY SO$',
    'I IZ': r'^I IZ$',
    'FOUND YR': r'^FOUND YR$',
    'GTFO': r'^GTFO$',
    
    # Miscellaneous
    'MKAY': r'^MKAY$',

    # Literals
    'numbr': r'^(\-?(0+)|\-?[1-9][0-9]*)$',
    'numbar': r'^\-?[0-9]+\.[0-9]+$',
    'yarn': r'^\"[^\"]*\"$',
    'troof': r'^(WIN|FAIL)$',
    'type': r'^(NUMBR|NUMBAR|YARN|TROOF|NOOB)$',

    # Identifiers
    'varident': r'^[A-Za-z][A-Za-z0-9_]*$',
    'funcident': r'^[A-Za-z][A-Za-z0-9_]*$',
    'loopident': r'^[A-Za-z][A-Za-z0-9_]*$',
}
