from parser_tokens import REGEX_TOKENS
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
            tokens.append(("OBTW", "OBTW"))
            
            if len(line) > 4:
                tokens.append((line[4:], "text"))
             
            tokens.append(("\\n", "linebreak"))

            line_number += 1
            
            if line_number == len(lines):
                raise Exception("TLDR not found")

            line = lines[line_number].strip()

            while line_number < len(lines) and not line.endswith("TLDR"):
                tokens.append((line, "text"))
                tokens.append(("\\n", "linebreak"))
                line_number += 1

                if line_number == len(lines):
                    raise Exception("TLDR not found")

                line = lines[line_number].strip()

            if line.endswith("TLDR"):
                if len(line) > 4:
                    tokens.append((line[:-4], "text"))
                tokens.append(("TLDR", "TLDR"))
                tokens.append(("\\n", "linebreak"))
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
                        for other in token.split():
                            expanded_words.append(other)
        
        print(expanded_words);

        i = 0

        while i < len(expanded_words):
            matched = False

            for j in range(len(expanded_words) - 1, i - 1, -1):
                current = " ".join(expanded_words[i:j + 1])

                for word_type, pattern in REGEX_TOKENS.items():
                    regex = re.compile(pattern)

                    if regex.fullmatch(current):
                        if word_type == "BTW":
                            tokens.append(("BTW", "BTW"))

                            if len(current) > 3:
                                tokens.append((current[3:], "text"))
                        else:
                            tokens.append((current, word_type))
                        
                        matched = True
                        i = j + 1
                        break

                if matched:
                    break

            if not matched:
                print(expanded_words[i])
                print("BAD TOKEN")
                return tokens

        line_number += 1
        tokens.append(("\\n", "linebreak"))
    
    print(tokens)
    return tokens
