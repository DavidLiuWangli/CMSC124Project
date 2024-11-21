from lexer import lexical_analyzer
from grammars import GRAMMARS

def parse(non_terminal, tokens, position):
    global scanned_lexemes

    for production in GRAMMARS[non_terminal]:
        current_position = position
        success = True
        for symbol in production:
            if symbol in GRAMMARS:
                result, current_position = parse(symbol, tokens, current_position)
                if not result:
                    success = False
                    break
            elif symbol == '':
                continue
            else:
                if current_position < len(tokens) and tokens[current_position][1] == symbol:
                    print(current_position, symbol, GRAMMARS[non_terminal])
                    current_position += 1
                else:
                    success = False
                    break

        if success:
            return True, current_position

    return False, position

def main():
    code = ""
    with open("../../lolcode_test_cases/" + input(), 'r') as file:
        code = file.read()

    tokens = lexical_analyzer(str(code))
    
    result, final_position = parse("program", tokens, 0)

    if result and final_position == len(tokens):
        print("Parsing succeeded!")
    else:
        print("Unexpected token:", tokens[final_position])

if __name__ == "__main__":
    main()
