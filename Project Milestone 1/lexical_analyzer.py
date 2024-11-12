from tokens import TOKENS
import re

# Does not work?
def lexical_analyzer(code):
    tokens = []
    lines = code.splitlines()
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()  # Remove leading/trailing whitespace
        if not line:
            continue  # Skip empty lines
        match_found = False
        for token_type, pattern in TOKENS.items():
            regex = re.compile(pattern)
            match = regex.match(line)
            if match:
                lexeme = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, lexeme))
                match_found = True
                break
        if not match_found:
            print(f"Error: Unexpected content on line {line_number}: '{line}'")
            raise ValueError(f'Unexpected content on line {line_number}: "{line}"')
    return tokens

def read_code_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_tokens_file(tokens, filename):
    with open(filename, 'w') as file:
        for token_type, lexeme in tokens:
            file.write(f"{token_type}: {lexeme}\n")

sample_code = read_code_file("sample_lolcode.lol")
tokens = lexical_analyzer(sample_code)
write_tokens_file(tokens, "sample_tokens.txt")
