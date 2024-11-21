import sys
from lexer import lexical_analyzer
from grammars import GRAMMARS

def parse(non_terminal, tokens, position):
    global scanned_lexemes
    """
    Recursive function to parse a sequence of tokens based on the grammar rules
    defined in GRAMMARS.
    
    Args:
        non_terminal (str): The current non-terminal to parse.
        tokens (list): A list of token tuples produced by the lexical analyzer.
        position (int): The current position in the tokens list.

    Returns:
        (bool, int): A tuple where the first element indicates success (True/False)
        and the second element is the updated token position.
    """

    # Iterate over all productions for the current non-terminal.
    for production in GRAMMARS[non_terminal]:
        current_position = position
        success = True
        # Check each symbol in the production.
        for symbol in production:
            if symbol in GRAMMARS:  # Non-terminal
                result, current_position = parse(symbol, tokens, current_position)
                if not result:
                    success = False
                    break
            elif symbol == '':  # Epsilon production.
                continue
            else:  # Terminal
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
    global scanned_lexemes
    # Read the code from a file.
    code = ""
    with open("../../lolcode_test_cases/" + input(), 'r') as file:
        code = file.read()

    # Generate tokens using the lexical analyzer.
    tokens = lexical_analyzer(str(code))


    # Parse the tokens starting from the initial non-terminal.
    result, final_position = parse("program", tokens, 0)

    # Check if parsing succeeded and all tokens were consumed.
    if result and final_position == len(tokens):
        print("Parsing succeeded!")
    else:
        print("Unexpected token:", tokens[final_position])

if __name__ == "__main__":
    main()

