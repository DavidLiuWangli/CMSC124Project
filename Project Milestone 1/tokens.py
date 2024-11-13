import re


TOKENS = {

    # Literals
    'NUMBR_LITERAL': r'^(\-?(0+)|\-?[1-9][0-9]*)$',
    'NUMBAR_LITERAL': r'^\-?([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)$',
    'YARN_LITERAL': r'^\"[^\"]*\"$',
    'TROOF_LITERAL': r'^(WIN|FAIL)$',
    'TYPE_LITERAL': r'^(NUMBR|NUMBAR|YARN|TROOF|NOOB)$',

    # Keywords
    'PROGRAM_START': r'^HAI$',
    'PROGRAM_END': r'^KTHXBYE$',
    'DATA_SECTION_START': r'^WAZZUP$',
    'DATA_SECTION_END': r'^BUHBYE$',
    'COMMENT': r'^BTW.*$',
    'MULTI_LINE_COMMENT_START': r'^OBTW$',
    'MULTI_LINE_COMMENT_END': r'^TLDR$',
    'VAR_DECL': r'^I HAS A$',
    'ITZ': r'^ITZ$',
    'ASSIGNMENT': r'^R$',
    
    # Arithmetic operations
    'SUM_OF': r'^SUM OF$',
    'DIFF_OF': r'^DIFF OF$',
    'PRODUKT_OF': r'^PRODUKT OF$',
    'QUOSHUNT_OF': r'^QUOSHUNT OF$',
    'MOD_OF': r'^MOD OF$',
    'BIGGR_OF': r'^BIGGR OF$',
    'SMALLR_OF': r'^SMALLR OF$',

    # Boolean operations
    'BOTH_OF': r'^BOTH OF$',
    'EITHER_OF': r'^EITHER OF$',
    'WON_OF': r'^WON OF$',
    'NOT': r'^NOT$',

    # Any/All expressions
    'ANY_OF': r'^ANY OF$',
    'ALL_OF': r'^ALL OF$',

    # Comparison
    'BOTH_SAEM': r'^BOTH SAEM$',
    'DIFFRINT': r'^DIFFRINT$',

    # Concatenation
    'SMOOSH': r'^SMOOSH$',

    # Typecasting
    'MAEK': r'^MAEK$',
    'A': r'^A$',
    'IS_NOW_A': r'^IS NOW A$',

    # Input/Output
    'VISIBLE': r'^VISIBLE$',
    'GIMMEH': r'^GIMMEH$',

    # Conditionals
    'IF_START': r'^O RLY\?$',
    'IF_TRUE': r'^YA RLY$',
    'IF_ELSE': r'^MEBBE$',
    'IF_FALSE': r'^NO WAI$',
    'IF_END': r'^OIC$',

    # Switch-case
    'SWITCH_START': r'^WTF\?$',
    'CASE': r'^OMG$',
    'DEFAULT_CASE': r'^OMGWTF$',

    # Loops
    'LOOP_START': r'^IM IN YR$',
    'LOOP_INCREMENT': r'^UPPIN$',
    'LOOP_DECREMENT': r'^NERFIN$',
    'LOOP_VAR': r'^YR$',
    'LOOP_CONDITION_TIL': r'^TIL$',
    'LOOP_CONDITION_WILE': r'^WILE$',
    'LOOP_END': r'^IM OUTTA YR$',

    # Functions
    'FUNC_DECL': r'^HOW IZ I$',
    'FUNC_END': r'^IF U SAY SO$',
    'FUNC_CALL': r'^I IZ$',
    'RETURN': r'^FOUND YR$',
    'EXIT': r'^GTFO$',

    # Identifiers
    'VARIABLE_IDENTIFIER': r'^[A-Za-z][A-Za-z0-9_]*$',
    'FUNCTION_IDENTIFIER': r'^[A-Za-z][A-Za-z0-9_]*$',
    'LOOP_IDENTIFIER': r'^[A-Za-z][A-Za-z0-9_]*$',
    
    # Miscellaneous
    'MKAY': r'^MKAY$',
    'NEWLINE': r'\n+',
    'WHITESPACE': r'^\s+'
}
