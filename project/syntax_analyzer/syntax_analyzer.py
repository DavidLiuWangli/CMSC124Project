from lexer import lexical_analyzer
from grammars import GRAMMARS

def parse(non_terminal, tokens, position):
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
                    break

        if success:
            return True, current_position, (non_terminal, subtree)

    return False, position, None

def main():
    code = ""
    with open("../../lolcode_test_cases/" + input(), 'r') as file:
        code = file.read()

    tokens = lexical_analyzer(str(code))
    
    result, final_position, parse_tree = parse("program", tokens, 0)
    
    print(parse_tree)

    if result and final_position == len(tokens):
        print("Parsing succeeded!")
    else:
        print("Unexpected token:", tokens[final_position])

if __name__ == "__main__":
    main()
