from pathlib import Path
from syntax_analyzer.lexical_analyzer import lexical_analyzer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.depth = 0
    
    def current_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None
    
    def next(self):
        if self.position < len(self.tokens):
            self.position += 1

<<<<<<< HEAD
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
                    if current_position < len(tokens):
                        unexpectedtoken = tokens[current_position][0]
                    break
=======
    def expect(self, token):
        self.last_expected = token
        if token == "":
            return True
        if self.current_token() and self.tokens[self.position][1] == token:
            # Successfully matched {self.current_token()} with {token}
            self.next()
            return True
        else:
            # Unsuccessful match {self.current_token()} with {token}
            self.unexpected_token = self.current_token()[0] if self.current_token() else "EOF"
            return False
>>>>>>> c7c19fefde1fb9709bd2dd417fbb4391f6b2d1f0

    def program(self):
        if self.outsides() and self.expect("HAI") and self.end_of_line() and self.data_section() and self.statements() and self.expect("KTHXBYE") and self.end_of_line() and self.outsides():
            return ""
        return f"{self.unexpected_token}"

    def outsides(self):
        if self.outside() and self.outsides():
            return True
        return self.expect("")

    def outside(self):
        if self.comment():
            return True
        if self.multi_line_comment():
            return True
        return False
    
    def statements(self):
        if self.statement() and self.statements():
            return True
        return self.expect("")

    def statement(self):
        if self.comment():
            return True
        if self.multi_line_comment():
            return True
        if self.input():
            return True
        if self.output():
            return True
        if self.variable_identifier() and self.variable_starting_statement():
            return True
        if self.expect("IT") and self.variable_assignment():
            return True
        if self.switch_case_block():
            return True
        if self.condition_block():
            return True
        if self.loop_block():
            return True
        if self.function_call():
            return True
        if self.function():
            return True
        return False

    def variable_starting_statement(self):
        if self.re_casting():
            return True
        if self.variable_assignment():
            return True
        if self.end_of_line() and self.switch_case_block():
            return True
        return False

    def comment(self):
        if self.expect("BTW") and self.comment_text() and self.expect("linebreak"):
            return True
        return False

    def multi_line_comment(self):
        if self.expect("OBTW") and self.comment_text() and self.expect("linebreak") and self.multi_content() and self.comment_text() and self.expect("TLDR") and self.end_of_line():
            return True
        return False

    def multi_content(self):
        if self.comment_text() and self.expect("linebreak") and self.multi_content():
            return True
        return self.expect("")

    def data_section(self):
        if self.expect("WAZZUP") and self.end_of_line() and self.declarations() and self.expect("BUHBYE") and self.end_of_line():
            return True
        return self.expect("")

    def declarations(self):
        if self.expect("I HAS A") and self.variable_identifier() and self.initialization() and self.end_of_line() and self.declarations():
            return True
        if self.end_of_line() and self.declarations():
            return True
        return self.expect("")

    def initialization(self):
        if self.expect("ITZ") and self.value():
            return True
        return self.expect("")

    def value(self):
        if self.literal():
            return True
        if self.expression():
            return True
        if self.variable_identifier():
            return True
        return False

    def literal(self):
        if self.expect("numbr"):
            return True
        if self.expect("numbar"):
            return True
        if self.expect("yarn"):
            return True
        if self.expect("troof"):
            return True
        return False

    def expression(self):
        if self.math_expression():
            return True
        if self.concatenation():
            return True
        if self.boolean_expression():
            return True
        if self.comparison_expression():
            return True
        if self.all_any_expression():
            return True
        if self.typecasting():
            return True
        return False

    def input(self):
        if self.expect("GIMMEH") and self.variable_identifier() and self.end_of_line():
            return True
        if self.expect("GIMMEH") and self.expect("IT") and self.end_of_line():
            return True
        return False

    def output(self):
        if self.expect("VISIBLE") and self.operand() and self.output_operands() and self.end_of_line():
            return True
        return False

    def output_operands(self):
        if self.expect("+") and self.operand() and self.output_operands():
            return True
        if self.expect("AN") and self.operand() and self.output_operands():
            return True
        if self.operand() and self.output_operands():
            return True
        return self.expect("")

    def operand(self):
        if self.variable_identifier():
            return True
        if self.literal():
            return True
        if self.expect("IT"):
            return True
        if self.expression():
            return True
        return False

    def math_expression(self):
        if self.math_operator() and self.operand() and self.expect("AN") and self.operand():
            return True
        return False

    def math_operator(self):
        if self.expect("SUM OF"):
            return True
        if self.expect("DIFF OF"):
            return True
        if self.expect("PRODUKT OF"):
            return True
        if self.expect("QUOSHUNT OF"):
            return True
        if self.expect("MOD OF"):
            return True
        return False

    def concatenation(self):
        if self.expect("SMOOSH") and self.operand() and self.concatenation_operands():
            return True
        return False

    def concatenation_operands(self):
        if self.expect("AN") and self.operand() and self.concatenation_operands():
            return True
        return self.expect("")

    def boolean_expression(self):
        if self.boolean_operator() and self.operand() and self.expect("AN") and self.operand():
            return True
        if self.expect("NOT") and self.operand():
            return True
        return False

    def boolean_operator(self):
        if self.expect("BOTH OF"):
            return True
        if self.expect("EITHER OF"):
            return True
        if self.expect("WON OF"):
            return True
        return False

    def comparison_expression(self):
        if self.comparison_operator() and self.operand() and self.expect("AN") and self.operand():
            return True
        return False

    def comparison_operator(self):
        if self.expect("BOTH SAEM"):
            return True
        if self.expect("DIFFRINT"):
            return True
        if self.expect("BIGGR OF"):
            return True
        if self.expect("SMALLR OF"):
            return True
        return False

    def inequality(self):
        if self.expect("BIGGR OF") and self.operand() and self.expect("AN"):
            return True
        if self.expect("SMALLR OF") and self.operand() and self.expect("AN"):
            return True
        return self.expect("")

    def all_any_expression(self):
        if self.all_any_operator() and self.all_any_operand() and self.all_any_operands() and self.expect("MKAY"):
            return True
        return False

    def all_any_operator(self):
        if self.expect("ALL OF"):
            return True
        if self.expect("ANY OF"):
            return True
        return False
    
    def all_any_operands(self):
        if self.expect("AN") and self.all_any_operand() and self.all_any_operands():
            return True
        return self.expect("")

    def all_any_operand(self):
        if self.variable_identifier():
            return True
        if self.literal():
            return True
        if self.expect("IT"):
            return True
        if self.all_any_math():
            return True
        if self.all_any_boolean():
            return True
        if self.all_any_concatenation():
            return True
        if self.all_any_comparison():
            return True
        return False

    def all_any_math(self):
        if self.math_operator() and self.all_any_operand() and self.expect("AN") and self.all_any_operand():
            return True
        return False

    def all_any_boolean(self):
        if self.boolean_operator() and self.all_any_operand() and self.expect("AN") and self.all_any_operand():
            return True
        if self.expect("NOT") and self.all_any_operand():
            return True
        return False

    def all_any_concatenation(self):
        if self.expect("SMOOSH") and self.all_any_operand() and self.all_any_concatenation_operands():
            return True
        return False

    def all_any_concatenation_operands(self):
        if self.expect("AN") and self.all_any_operand() and self.all_any_concatenation_operands():
            return True
        return self.expect("")

    def all_any_comparison(self):
        if self.comparison_operator() and self.all_any_operand() and self.expect("AN") and self.inequality() and self.all_any_operand():
            return True
        return False

    def typecasting(self):
        if self.expect("MAEK") and self.variable_identifier() and self.typecasting_separator() and self.expect("type"):
            return True
        return False

    def typecasting_separator(self):
        if self.expect("A"):
            return True
        return self.expect("")

    def re_casting(self):
        if self.expect("IS NOW A") and self.expect("type") and self.end_of_line():
            return True
        return False

    def variable_assignment(self):
        if self.expect("R") and self.value() and self.end_of_line():
            return True
        return False

    def condition_block(self):
        if self.expression() and self.end_of_line() and self.expect("O RLY?") and self.end_of_line() and self.expect("YA RLY") and self.end_of_line() and self.statements() and self.else_if_chain() and self.else_block() and self.expect("OIC") and self.end_of_line():
            return True
        return False

    def else_if_chain(self):
        if self.else_if_block() and self.else_if_chain():
            return True
        return self.expect("")

    def else_if_block(self):
        if self.expect("MEBBE") and self.expression() and self.end_of_line() and self.statements():
            return True
        return False

    def else_block(self):
        if self.expect("NO WAI") and self.end_of_line() and self.statements():
            return True
        return self.expect("")

    def switch_case_block(self):
        if self.expect("WTF?") and self.end_of_line() and self.cases_chain() and self.default_case_block() and self.expect("OIC") and self.end_of_line():
            return True
        return False

    def cases_chain(self):
        if self.case_block() and self.cases_chain():
            return True
        return self.expect("")

    def case_block(self):
        if self.expect("OMG") and self.literal() and self.end_of_line() and self.control_body():
            return True
        return False

    def default_case_block(self):
        if self.expect("OMGWTF") and self.end_of_line() and self.control_body():
            return True
        return self.expect("")

    def control_body(self):
        if self.expect("GTFO") and self.end_of_line():
            return True
        if self.statement() and self.control_body():
            return True
        return self.expect("")

    def loop_block(self):
        if self.expect("IM IN YR") and self.loop_identifier() and self.loop_direction() and self.expect("YR") and self.variable_identifier() and self.loop_condition() and self.end_of_line() and self.control_body() and self.expect("IM OUTTA YR") and self.loop_identifier() and self.end_of_line():
            return True
        return False
    
    def loop_direction(self):
        if self.expect("UPPIN"):
            return True
        if self.expect("NERFIN"):
            return True
        return False

    def loop_condition(self):
        if self.expect("TIL") and self.expression():
            return True
        if self.expect("WILE") and self.expression():
            return True
        return False

    def function(self):
        if self.expect("HOW IZ I") and self.function_identifier() and self.parameters() and self.end_of_line() and self.function_body() and self.expect("IF U SAY SO") and self.end_of_line():
            return True
        return False

    def function_call(self):
        if self.expect("I IZ") and self.function_identifier() and self.arguments() and self.expect("MKAY") and self.end_of_line():
            return True
        return False

    def parameters(self):
        if self.expect("YR") and self.variable_identifier() and self.extra_parameters():
            return True
        return self.expect("")

    def extra_parameters(self):
        if self.expect("AN") and self.expect("YR") and self.variable_identifier() and self.extra_parameters():
            return True
        return self.expect("")

    def arguments(self):
        if self.expect("YR") and self.value() and self.extra_arguments():
            return True
        return self.expect("")

    def extra_arguments(self):
        if self.expect("AN") and self.expect("YR") and self.value() and self.extra_arguments():
            return True
        return self.expect("")

    def return_function(self):
        if self.expect("FOUND YR") and self.value() and self.end_of_line():
            return True
        if self.expect("GTFO") and self.end_of_line():
            return True
        return False

    def function_body(self):
        if self.statement() and self.function_body():
            return True
        if self.return_function() and self.function_body():
            return True
        return self.expect("")

    def end_of_line(self):
        if self.comment():
            return True
        if self.expect("linebreak"):
            return True
        return False

    def comment_text(self):
        if self.expect("text"):
            return True
        return self.expect("")

    def variable_identifier(self):
        if self.expect("varident"):
            return True
        return False

    def function_identifier(self):
        if self.expect("varident"):
            return True
        return False

    def loop_identifier(self):
        if self.expect("varident"):
            return True
        return False

def syntax_analyzer(code):
    tokens = lexical_analyzer(code)
    parser = Parser(tokens)
    token = parser.program()
    if (token == ""):
        return ""
    else:
        line_number = 0
        lines = code.split('\n')
        for number, line in enumerate(lines, start=1):
            if token in line:
                line_number = number
                break
        return f"Unexpected token: {token} at line number {line_number}"
        
