from pathlib import Path
from lexical_analyzer import lexical_analyzer

class Parser:
    def __init__(self, tokens):
        # print(tokens)
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

    def expect(self, token):
        self.last_expected = token
        if token == "":
            # print("Skipping token")
            return True
        if self.current_token() and self.tokens[self.position][1] == token:
            # print(f"Successfully matched {self.current_token()} with {token}")
            self.next()
            return True
        else:
            # print(f"Unsuccessful match {self.current_token()} with {token}")
            self.unexpected_token = self.current_token()[0] if self.current_token() else "EOF"
            return False

    def program(self):
        if self.outsides() and self.expect("HAI") and self.end_of_line() and self.data_section() and self.statements() and self.expect("KTHXBYE") and self.end_of_line() and self.outsides():
            return True
        raise Exception(f"Unexpected token: {self.unexpected_token}, expecting: {self.last_expected}")

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
        # print("Entered statments!")
        if self.statement() and self.statements():
            return True
        return self.expect("")

    def statement(self):
        # print("Entered statement!")
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
        # print("Exiting statement!")
        return False

    def variable_starting_statement(self):
        # print("Entered variable starting!")
        if self.re_casting():
            return True
        if self.variable_assignment():
            # print("IS variable assignment!")
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
        # print("Entered function!")
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

def syntax_analyzer(tokens):
    parser = Parser(tokens)
    return parser.program()

def main():
    passed_all_test_cases = True
    test_cases_folder = Path("../../lolcode_test_cases")
    for file_path in sorted(test_cases_folder.glob("*.lol")):  # Adjust the pattern if needed
        filename = file_path.name
        print(f"Processing file: {filename}")
        with open(file_path, "r") as file:
            code = file.read()
        tokens = lexical_analyzer(code)  # Call your lexical analyzer
        if not syntax_analyzer(tokens):
            passed_all_test_cases = False
            print(f"Failed at testcase: {filename}")
            break
    if passed_all_test_cases:
        print("Passed all test cases.")
if __name__ == "__main__":
    main()
