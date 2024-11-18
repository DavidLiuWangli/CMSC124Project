from tokens import KEYWORDS, LITERALS, IDENTIFIERS
import re

def lexical_analyzer(code):
    tokens = []
    liness = code.splitlines()
    lines = []
    index = 0
    while index < len(liness):
        liness[index] = liness[index].strip()
        if len(liness[index]) >= 4 and liness[index][0:4] == "OBTW":
            while not (len(liness[index]) >= 4 and liness[index][-4:] == "TLDR"):
                index += 1
        else:
            lines.append(liness[index])
        index += 1
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        special = r'\"[^\"]*\"|BTW\s.*|\S+'
        wordss = re.findall(special, line) # I HAS A "hello  world" PRODUCT OF BTW    hello -> I HAS A, "hello  world", PRODUCT OF BTW     hello
        # print(wordss)
        words = []
        for word in wordss:
            if word[0] == '"':
                words.append(word)
            else:
                special_BTW = r'BTW\s.*|\S+'
                yay = re.findall(special_BTW, word)
                print(yay)
                for worded in yay:
                    if len(worded) >= 3 and worded[0:3] == "BTW":
                        words.append(worded)
                    else:
                        for wordedness in worded.split():
                            words.append(wordedness)
        print("WORDS:", words)
        i = 0
        while i < len(words):
            matched_any = False
            for j in range(len(words) - 1, i - 1, -1):
                current = " ".join(words[i:j+1])
                print(current)
                matched = False
                for keyword_type, pattern in KEYWORDS.items():
                    # print(pattern)
                    regex = re.compile(pattern)
                    if regex.fullmatch(current):
                        tokens.append((keyword_type, current))
                        matched = True
                        break
                if matched:
                    matched_any = True
                    i = j + 1
                    break
                for literal_type, pattern in LITERALS.items():
                    regex = re.compile(pattern)
                    if regex.fullmatch(current):
                        tokens.append((literal_type, current))
                        matched = True
                        break
                if matched:
                    matched_any = True
                    i = j + 1
                    break
                for identifier_type, pattern in IDENTIFIERS.items():
                    regex = re.compile(pattern)
                    if regex.fullmatch(current):
                        tokens.append((identifier_type, current))
                        matched = True
                        break
                if matched:
                    matched_any = True
                    i = j + 1
                    break
            if not matched_any:
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

path = input()
sample_code = read_code_file(path)
tokens = lexical_analyzer(sample_code)
write_tokens_file(tokens, "output.txt")
