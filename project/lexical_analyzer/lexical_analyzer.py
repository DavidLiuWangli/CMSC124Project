from tokens import REGEX_MAP
import re

def lexical_analyzer(code):
    tokens = []
    lines = code.splitlines()
    
    line_number = 0

    while line_number < len(lines):
        line = lines[line_number].strip()
        
        # Handle empty lines
        if line == "":
            line_number += 1
            continue

        # Handle multi-line comments
        if line.startswith("OBTW"):
            tokens.append(("MULTI_COMMENT_START", "OBTW"))
            
            if len(line) > 4:
                tokens.append(("COMMENT_TEXT", line[4:]))
            
            line_number += 1
            
            if line_number == len(lines):
                raise Exception("TLDR not found")

            line = lines[line_number].strip()

            while line_number < len(lines) and not line.endswith("TLDR"):
                tokens.append(("COMMENT_TEXT", line))
                line_number += 1

                if line_number == len(lines):
                    raise Exception("TLDR not found")

                line = lines[line_number].strip()

            if line.endswith("TLDR"):
                tokens.append(("COMMENT_TEXT", line[-4:]))
                tokens.append(("MULTI_COMMENT_END", "TLDR"))
            else:
                raise Exception("TLDR not found")

            line_number += 1
            continue
        
        # Make sure to split the line with strings and comments intact
        special_pattern = r'\"[^\"]*\"|BTW\s.*|\S+'
        words = re.findall(special_pattern, line)

        expanded_words = []

        for word in words:
            if word.startswith('"'):
                expanded_words.append(word)
            else:
                sub_tokens = re.findall(r'BTW\s.*|\S+', word)

                for token in sub_tokens:
                    if token.startswith("BTW"):
                        expanded_words.append(token)
                    else:
                        expanded_words.extend(token.split())

        i = 0

        while i < len(expanded_words):
            matched = False

            for j in range(min(i + 4, len(expanded_words) - 1), i - 1, -1):
                current = " ".join(expanded_words[i:j + 1])

                for word_type, pattern in REGEX_MAP.items():
                    regex = re.compile(pattern)

                    if regex.fullmatch(current):
                        if word_type == "COMMENT":
                            tokens.append(("COMMENT_START", "BTW"))

                            if len(current) > 3:
                                tokens.append(("COMMENT_TEXT", current[4:]))
                        else:
                            tokens.append((word_type, current))
                        
                        matched = True
                        i = j + 1
                        break

                if matched:
                    break

            if not matched:
                print("BAD TOKEN")
                return tokens

        line_number += 1
        tokens.append(("NEWLINE", "\\n"))

    return tokens

def read_code_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_tokens_file(tokens, filename):
    with open(filename, 'w') as file:
        for token_type, lexeme in tokens:
            file.write(f"{token_type}: {lexeme}\n")

if __name__ == "__main__":
    path = input()
    sample_code = read_code_file(path)
    tokens = lexical_analyzer(sample_code)
    write_tokens_file(tokens, "output.txt")
