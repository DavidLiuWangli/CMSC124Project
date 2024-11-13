from tokens import TOKENS
import re

def lexical_analyzer(code):
    tokens = []
    lines = code.splitlines()
    regexes = {}
    
    for token_type, pattern in TOKENS.items():
        regexes[token_type] = re.compile(pattern)
        
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if not line: 
            continue
        segments = re.findall(r'"[^"]*"|[A-Za-z][A-Za-z0-9_ ]*', line)
        
        for segment in segments:
            matched = False
            
            for token_type, regex in regexes.items():
                match = regex.fullmatch(segment.strip())
                if match:
                    if token_type != 'WHITESPACE':
                        tokens.append((token_type, segment))
                    matched = True
                    break
                
            if not matched:
                print(f"Error: Unexpected content on line {line_number}: '{segment}'")
                break
            
        tokens.append(("NEWLINE", "\\n"))

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
