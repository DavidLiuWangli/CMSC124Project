from lexer import lexical_analyzer
from grammars import GRAMMARS

reacted = 0

def parse(non_terminal, tokens, position):
    global reacted
    print("TERMINAL")
    if position >= len(tokens):
        return False, position
    print(tokens[position], non_terminal)
    print("GRAMMARS: ", GRAMMARS[non_terminal]);
    for production in GRAMMARS[non_terminal]:
        print("PRODUCTION")
        print(production)
        current_position = position
        success = True
        for symbol in production:
            if symbol in GRAMMARS:  # Non-terminal
                result, current_position = parse(symbol, tokens, current_position)
                if not result:
                    success = False
                    break
            else:  # Terminal
                if symbol == '':
                    continue
                if current_position < len(tokens) and tokens[current_position][1] == symbol:
                    print("REACTED: ", symbol)
                    current_position += 1
                    reacted += 1
                else:
                    print("NOOOOOOOO", symbol)
                    success = False
                    break
        if success:
            return True, current_position
    return False, position

tokens = lexical_analyzer("OBTW what is     happening\ntaalga baaa hahahaha a ah    aa\nTLDR\nHAI\nVISIBLE 1\nKTHXBYE\n")
print(tokens)
result, final_position = parse("program", tokens, 0)
print(reacted)
if reacted == len(tokens):
    print("Parsing succeeded!")
else:
    print("Parsing failed.")

