from tokens import KEYWORDS, LITERALS, IDENTIFIERS
import re

def lexical_analyzer(code):
    tokens = []
    lines = []
    
    code_lines = code.splitlines()
    index = 0

    while index < len(code_lines):
        line = code_lines[index].strip()

        if line.startswith("OBTW"):
            while index < len(code_lines) and not line.endswith("TLDR"):
                index += 1
                line = code_lines[index].strip() if index < len(code_lines) else ""
        else:
            lines.append(line)
        index += 1

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
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

                for REGEX_MAP in [KEYWORDS, LITERALS, IDENTIFIERS]:
                    for word_type, pattern in REGEX_MAP.items():
                        regex = re.compile(pattern)

                        if regex.fullmatch(current):
                            tokens.append((word_type, current))
                            matched = True
                            i = j + 1
                            break

                    if matched:
                        break

                if matched:
                    break

            if not matched:
                print("BAD TOKEN")
                return tokens
    
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
