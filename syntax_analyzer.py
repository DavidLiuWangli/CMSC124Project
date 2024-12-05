from syntax_analyzer.lexical_analyzer import lexical_analyzer
from syntax_analyzer.grammars import GRAMMARS

unexpectedtoken = ""

def parse(non_terminal, tokens, position):
    global unexpectedtoken
    
    for production in GRAMMARS[non_terminal]:
        current_position = position
        success = True
        subtree = []

        for symbol in production:
            if symbol in GRAMMARS:
                result, current_position, child_tree = parse(symbol, tokens, current_position)
                if not result:
                    success = False
                    break
                subtree.append((symbol, child_tree))
            elif symbol == '':
                continue
            else:
                if current_position < len(tokens) and tokens[current_position][1] == symbol:
                    print(current_position, symbol, GRAMMARS[non_terminal])
                    subtree.append(tokens[current_position])
                    current_position += 1
                else:
                    success = False
                    if current_position < len(tokens):
                        unexpectedtoken = tokens[current_position][0]
                    break

        if success:
            return True, current_position, (non_terminal, subtree)

    return False, position, None

def syntax_analyzer(code):

    tokens = lexical_analyzer(code)
    
    result, final_position, parse_tree = parse("program", tokens, 0)

    if result and final_position == len(tokens):
        return str(parse_tree) + "\nParsing succeeded!"
    else:
        return str(parse_tree) + "\nUnexpected token: " + unexpectedtoken
