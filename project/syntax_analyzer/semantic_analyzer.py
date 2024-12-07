from parser_tokens import REGEX_TOKENS
import re
from pathlib import Path
from lexical_analyzer import lexical_analyzer

def typecast_string(value):
    if value == None:
        return "NOOB"

    if type(value) == bool:
        if value:
            return "WIN"
        else:
            return "FAIL"

    return str(value)

def math_operand_re_cast(operand, operand_type):
    if operand_type not in ["numbr", "numbar"]:
        if operand_type == "noob":
            raise Exception(f"Cannot implicitly typecast NOOB to NUMBR or NUMBAR")
        elif operand_type == "troof":
            return int(operand)
        elif re.match(REGEX_TOKENS["numbr"], operand):
            return int(operand)
        elif re.match(REGEX_TOKENS["numbar"], operand):
            return float(operand)
        else:
            raise Exception(f"Cannot typecast {operand} to NUMBR or NUMBAR")
    
    return operand

def arithmetic_operation(operator, operand_1, operand_2):
    if operator == "SUM OF":
        return operand_1 + operand_2
    elif operator == "DIFF OF":
        return operand_1 - operand_2
    elif operator == "PRODUKT OF":
        return operand_1 * operand_2
    elif operator == "QUOSHUNT OF":
        if type(operand_1) == int and type(operand_1) == int:
            return operand_1 // operand_2
        else:
            return operand_1 / operand_2
    elif operator == "MOD OF":
        return operand_1 % operand_2
    elif operator == "BIGGR OF":
        return max(operand_1, operand_2)
    elif operator == "SMALLR OF":
        return min(operand_1, operand_2)
    else:
        return None

class SyntaxSemanticAnalyzer:
    def __init__(self, tokens):
        # print(tokens)
        self.tokens = tokens
        self.position = 0
        self.depth = 0
        self.symbol_table = {}
        self.execute = True

    def previous_token(self, index=-1):
        if 0 <= self.position + index and self.position + index < len(self.tokens):
            return self.tokens[self.position + index][0]
        
        return None

    def previous_type(self, index=-1):
        if 0 <= self.position + index and self.position + index < len(self.tokens):
            return self.tokens[self.position + index][1]
        
        return None

    def current_token(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        
        return None
    
    def next(self):
        if self.position < len(self.tokens):
            self.position += 1

    def expect(self, token_type, token_value=None):
        if token_value == "NOOB" and self.current_token() and self.tokens[self.position][0] == "NOOB":
            self.next()
            return True

        self.last_expected = token_type
        
        if token_type == "":
            # print("Skipping token")
            return True
        elif self.current_token() and self.tokens[self.position][1] == token_type:
            # print(f"Successfully matched {self.current_token()} with {token}")
            self.next()
            return True
        else:
            # print(f"Unsuccessful match {self.current_token()} with {token}")
            if self.current_token():
                self.unexpected_token = self.current_token()[0]
            else:
                self.unexpected_token = "EOF"
            
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
        # print("EXECUTE:", self.execute)
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
        
        if self.variable_identifier():
            self.current_variable = self.previous_token()
            
            if self.variable_starting_statement():
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
        if self.expect("I HAS A") and self.variable_identifier():
            declaration_variable = self.current_variable

            if self.initialization():
                self.symbol_table[declaration_variable] = self.current_value
                
                if self.end_of_line() and self.declarations():
                    # print(self.current_variable, self.current_assign_value)
                    return True
        
        if self.end_of_line() and self.declarations():
            return True
        
        return self.expect("")

    def initialization(self):
        if self.expect("ITZ") and self.value():
            return True
        
        self.current_value = None
        return self.expect("")

    def value(self):
        if self.literal():
            self.current_value = self.current_literal
            return True
        
        if self.expression():
            self.current_value = self.current_expression
            return True
        
        if self.variable_identifier():
            self.current_value = self.symbol_table[self.current_variable]
            return True
        
        return False

    def literal(self):
        if self.expect("numbr"):
            self.current_literal = int(self.previous_token())
            return True
        
        if self.expect("numbar"):
            self.current_literal = float(self.previous_token())
            return True
        
        if self.expect("yarn"):
            self.current_literal = str(self.previous_token()[1:-1])
            return True
        
        if self.expect("troof"):
            if self.previous_token() == "WIN":
                self.current_literal = True
            else:
                self.current_literal = False
            
            return True
        
        return False

    def expression(self):
        if self.math_expression():
            self.current_expression = self.current_math_expression
            return True
        
        if self.concatenation():
            self.current_expression = self.current_concatenation
            return True
        
        if self.boolean_expression():
            self.current_expression = self.current_boolean_expression
            return True
        
        if self.comparison_expression():
            self.current_expression = self.current_comparison_expression
            return True
        
        if self.all_any_expression():
            self.current_expression = self.current_all_any_expression
            return True
        
        if self.typecasting():
            self.current_expression = self.current_typecasting
            return True
        
        return False

    def input(self):
        if self.expect("GIMMEH") and self.variable_identifier():
            if self.end_of_line():
                if self.execute:
                    self.symbol_table[self.current_variable] = input()
                
                return True
        
        if self.expect("GIMMEH") and self.expect("IT") and self.end_of_line():
            if self.end_of_line():
                self.symbol_table["IT"] = input()
            
            return True
        
        return False

    def output(self):
        if self.expect("VISIBLE") and self.operand():
            self.current_output_string = typecast_string(self.current_operand)

            if self.output_operands() and self.end_of_line():
                if self.execute:
                    print(self.current_output_string)
                
                return True
        
        return False

    def output_operands(self):
        if self.expect("+") and self.operand():
            self.current_output_string += typecast_string(self.current_operand)
            
            if self.output_operands():
                return True
        
        return self.expect("")

    def set_current_type(self):
        if self.current_operand == None:
            self.current_type = "noob"
        elif type(self.current_operand) == int:
            self.current_type = "numbr"
        elif type(self.current_operand) == float:
            self.current_type = "numbar"
        elif type(self.current_operand) == str:
            self.current_type = "yarn"
        elif type(self.current_operand) == bool:
            self.current_type = "troof"

    def operand(self):
        if self.expect("type", "NOOB"):
            self.current_operand = None
            self.set_current_type()
            return True

        if self.variable_identifier():
            self.current_operand = self.symbol_table[self.previous_token()]
            self.set_current_type() 
            return True
        
        if self.literal():
            self.current_operand = self.current_literal 
            self.set_current_type() 
            return True
        
        if self.expect("IT"):
            self.current_oeprand = self.symbol_table["IT"]
            self.set_current_type()
            return True
        
        if self.expression():
            self.current_operand = self.current_expression
            self.set_current_type()
            return True
        
        return False

    def math_expression(self):
        if self.math_operator():
            operator = self.previous_token()
            
            if self.operand():
                operand_1 = self.current_operand
                type_1 = self.current_type
                
                if self.expect("AN") and self.operand():
                    if not self.execute:
                        self.current_math_expression = None
                        return True

                    operand_2 = self.current_operand
                    type_2 = self.current_type

                    # print(f"Operand 1: {operand_1} {type_1}, Operand 2: {operand_2} {type_2}")

                    operand_1 = math_operand_re_cast(operand_1, type_1)
                    operand_2 = math_operand_re_cast(operand_2, type_2)
                    self.current_math_expression = arithmetic_operation(operator, operand_1, operand_2) 
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
        
        if self.expect("BIGGR OF"):
            return True
        
        if self.expect("SMALLR OF"):
            return True
        
        return False 

    def boolean_expression(self):
        if self.boolean_operator():
            operator = self.previous_token()
            
            if self.operand():
                operand_1 = bool(self.current_operand)
            
                if self.expect("AN") and self.operand():
                    operand_2 = bool(self.current_operand)
                    
                    if operator == "BOTH OF":
                        self.current_boolean_expression = operand_1 and operand_2
                    elif operator == "EITHER OF":
                        self.current_boolean_expression = operand_1 or operand_2
                    elif operator == "WON OF":
                        self.current_boolean_expression = operand_1 ^ operand_2

                    return True
        
        if self.expect("NOT") and self.operand():
            self.current_boolean_expression = not bool(self.current_operand)
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
    
    def concatenation(self):
        if self.expect("SMOOSH") and self.concatenation_operand():
            self.current_concatenation = typecast_string(self.current_concatenation_operand) 
            
            if self.concatenation_operands():
                return True

        return False

    def set_current_concatenation_type(self):
        if self.current_concatenation_operand == None:
            self.current_concatenation_type = "noob"
        elif type(self.current_concatenation_operand) == int:
            self.current_concatenation_type = "numbr"
        elif type(self.current_concatenation_operand) == float:
            self.current_concatenation_type = "numbar"
        elif type(self.current_concatenation_operand) == str:
            self.current_concatenation_type = "yarn"
        elif type(self.current_concatenation_operand) == bool:
            self.current_concatenation_type = "troof"

    def concatenation_operand(self):
        if self.expect("type", "NOOB"):
            self.current_concatenation_operand = None
            self.set_current_concatenation_type()
            return True

        if self.variable_identifier():
            self.current_concatenation_operand = self.symbol_table[self.current_variable]
            self.set_current_concatenation_type()
            return True
        
        if self.literal():
            self.current_concatenation_operand = self.current_literal
            self.set_current_concatenation_type()
            return True
        
        if self.expect("IT"):
            self.current_concatenation_operand = self.symbol_table["IT"]
            self.set_current_concatenation_type()
            return True
        
        if self.concatenation_math():
            self.current_concatenation_operand = self.current_concatenation_math
            self.set_current_concatenation_type()
            return True
        
        if self.concatenation_boolean():
            self.current_concatenation_operand = self.current_concatenation_boolean
            self.set_current_concatenation_type()
            return True
        
        if self.concatenation_comparison():
            self.current_concatenation_operand = self.current_concatenation_comparison
            self.set_current_concatenation_type()
            return True
        
        return False
 
    def concatenation_operands(self):
        if self.expect("AN") and self.concatenation_operand():
            self.current_concatenation += typecast_string(self.current_concatenation_operand)
            
            if self.concatenation_operands():
                return True
        
        return self.expect("")

    def concatenation_math(self):
        if self.math_operator():
            operator = self.previous_token()

            if self.concatenation_operand():
                operand_1 = self.current_concatenation_operand
                type_1 = self.current_concatenation_type

                if self.expect("AN") and self.concatenation_operand():
                    operand_2 = self.current_concatenation_operand
                    type_2 = self.current_concatenation_type

                    operand_1 = math_operand_re_cast(operand_1, type_1)
                    operand_2 = math_operand_re_cast(operand_2, type_2)
                    arithmetic_operation(operator, operand_1, operand_2)
                    return True
        
        return False

    def concatenation_boolean(self):
        if self.boolean_operator():
            operator = self.previous_token()
            
            if self.concatenation_operand():
                operand_1 = bool(self.current_concatenation_operand)
            
                if self.expect("AN") and self.concatenation_operand():
                    operand_2 = bool(self.current_concatenation_operand)
                    
                    if operator == "BOTH OF":
                        self.current_concatenation_boolean = operand_1 and operand_2
                    elif operator == "EITHER OF":
                        self.current_concatenation_boolean = operand_1 or operand_2
                    elif operator == "WON OF":
                        self.current_concatenation_boolean = operand_1 ^ operand_2

                    return True
        
        if self.expect("NOT") and self.concatenation_operand():
            self.current_concatenation_boolean = not bool(self.current_concatenation_operand)
            return True

        return False

    def concatenation_comparison(self):
        if self.comparison_operator():
            current_operator = self.previous_token()
            
            if self.concatenation_operand():
                operand_1 = self.current_concatenation_operand

                if self.expect("AN") and self.concatenation_operand():
                    operand_2 = self.current_concatenation_operand

                    if current_operator == "BOTH SAEM":
                        self.concatenation_comparison = operand_1 == operand_2
                    elif current_operator == "DIFFRINT":
                        self.concatenation_comparison = operand_1 != operand_2
                    
                    return True
        
        return False

    def comparison_expression(self):
        if self.comparison_operator():
            current_operator = self.previous_token()

            if self.operand():
                operand_1 = self.current_operand

                if self.expect("AN") and self.operand():
                    operand_2 = self.current_operand
                    
                    # print(f"Comparing {operand_1} and {operand_2}")

                    if current_operator == "BOTH SAEM":
                        self.current_comparison_expression = (operand_1 == operand_2)
                    elif current_operator == "DIFFRINT":
                        self.current_comparison_expression = (operand_1 != operand_2)
                    
                    return True
        
        return False

    def comparison_operator(self):
        if self.expect("BOTH SAEM"):
            return True
        
        if self.expect("DIFFRINT"):
            return True
        
        return False

    def all_any_expression(self):
        if self.all_any_operator():

            if self.current_all_any_operator == "ALL OF":
                self.current_all_any_expression = True
            elif self.current_all_any_operator == "ANY OF":
                self.current_all_any_expression = False

            if self.all_any_operand():
                operand = bool(self.current_all_any_operand)

                if self.current_all_any_operator == "ALL OF":
                    self.current_all_any_expression = self.current_all_any_expression and operand
                elif self.current_all_any_operator == "ANY OF":
                    self.current_all_any_expression = self.current_all_any_expression or operand

                if self.all_any_operands() and self.expect("MKAY"):
                    return True
        
        return False

    def all_any_operator(self):
        if self.expect("ALL OF"):
            self.current_all_any_operator = "ALL OF"
            return True
        
        if self.expect("ANY OF"):
            self.current_all_any_operator = "ANY OF"
            return True
        
        return False
    
    def all_any_operands(self):
        if self.expect("AN") and self.all_any_operand():
            operand = bool(self.current_all_any_operand)

            if self.current_all_any_operator == "ALL OF":
                self.current_all_any_expression = self.current_all_any_expression and operand
            elif self.current_all_any_operator == "ANY OF":
                self.current_all_any_expression = self.current_all_any_expression or operand

            if self.all_any_operands():
                return True

        return self.expect("")

    def set_current_all_any_type(self):
        if self.current_all_any_operand == None:
            self.current_all_any_type = "noob"
        elif type(self.current_all_any_operand) == int:
            self.current_all_any_type = "numbr"
        elif type(self.current_all_any_operand) == float:
            self.current_all_any_type = "numbar"
        elif type(self.current_all_any_operand) == str:
            self.current_all_any_type = "yarn"
        elif type(self.current_all_any_operand) == bool:
            self.current_all_any_type = "troof"

    def all_any_operand(self):
        if self.expect("type", "NOOB"):
            self.current_all_any_operand = None
            self.set_current_all_any_type()
            return True

        if self.variable_identifier():
            self.current_all_any_operand = self.symbol_table[self.current_variable]
            self.set_current_all_any_type()
            return True
        
        if self.literal():
            self.current_all_any_operand = self.current_literal
            self.set_current_all_any_type()
            return True
        
        if self.expect("IT"):
            self.current_all_any_operand = self.symbol_table["IT"]
            self.set_current_all_any_type()
            return True
        
        if self.all_any_math():
            self.current_all_any_operand = self.current_all_any_math
            self.set_current_all_any_type()
            return True
        
        if self.all_any_boolean():
            self.current_all_any_operand = self.current_all_any_boolean
            self.set_current_all_any_type()
            return True
        
        if self.all_any_comparison():
            self.current_all_any_operand = self.current_all_any_comparison
            self.set_current_all_any_type()
            return True
        
        return False
    
    def all_any_math(self):
        if self.math_operator():
            operator = self.previous_token()

            if self.all_any_operand():
                operand_1 = self.current_all_any_operand
                type_1 = self.current_all_any_type

                if self.expect("AN") and self.all_any_operand():
                    operand_2 = self.current_all_any_operand
                    type_2 = self.current_all_any_type

                    operand_1 = math_operand_re_cast(operand_1, type_1)
                    operand_2 = math_operand_re_cast(operand_2, type_2)
                    arithmetic_operation(operator, operand_1, operand_2)
                    return True
        
        return False

    def all_any_boolean(self):
        if self.boolean_operator():
            operator = self.previous_token()
            
            if self.all_any_operand():
                operand_1 = bool(self.current_all_any_operand)
            
                if self.expect("AN") and self.all_any_operand():
                    operand_2 = bool(self.current_all_any_operand)
                    
                    if operator == "BOTH OF":
                        self.current_all_any_boolean = operand_1 and operand_2
                    elif operator == "EITHER OF":
                        self.current_all_any_boolean = operand_1 or operand_2
                    elif operator == "WON OF":
                        self.current_all_any_boolean = operand_1 ^ operand_2

                    return True
        
        if self.expect("NOT") and self.all_any_operand():
            self.current_all_any_boolean = not bool(self.current_all_any_operand)
            return True

        return False

    def all_any_comparison(self):
        if self.comparison_operator():
            current_operator = self.previous_token()
            
            if self.all_any_operand():
                operand_1 = self.current_all_any_operand

                if self.expect("AN") and self.all_any_operand():
                    operand_2 = self.current_all_any_operand

                    if current_operator == "BOTH SAEM":
                        self.all_any_comparison = operand_1 == operand_2
                    elif current_operator == "DIFFRINT":
                        self.all_any_comparison = operand_1 != operand_2
                    
                    return True
        
        return False

    def typecasting(self):
        if self.expect("MAEK") and self.variable_identifier() and self.typecasting_separator() and self.expect("type"):
            self.current_type_literal = self.previous_token()

            if self.current_type_literal == "TROOF":
                self.current_typecasting = bool(self.symbol_table[self.current_variable])
            elif self.current_type_literal == "NUMBAR":
                self.current_typecasting = float(self.symbol_table[self.current_variable])
            elif self.current_type_literal == "NUMBR":
                self.current_typecasting = int(self.symbol_table[self.current_variable])
            elif self.current_type_literal == "YARN":
                self.current_typecasting = typecast_string(self.symbol_table[self.current_variable])

            return True
        
        return False

    def typecasting_separator(self):
        if self.expect("A"):
            return True
        
        return self.expect("")

    def re_casting(self):
        if self.expect("IS NOW A") and self.expect("type"):
            self.current_type_literal = self.previous_token()
            
            if self.execute:
                if self.current_type_literal == "TROOF":
                    self.symbol_table[self.current_variable] = bool(self.symbol_table[self.current_variable])
                elif self.current_type_literal == "NUMBAR":
                    self.symbol_table[self.current_variable] = float(self.symbol_table[self.current_variable])
                elif self.current_type_literal == "NUMBR":
                    self.symbol_table[self.current_variable] = int(self.symbol_table[self.current_variable])
                elif self.current_type_literal == "YARN":
                    self.symbol_table[self.current_variable] = typecast_string(self.symbol_table[self.current_variable])

            if self.end_of_line():
                return True
        
        return False

    def variable_assignment(self):
        if self.expect("R") and self.value():
            if self.execute:
                self.symbol_table[self.current_variable] = self.current_value 
            if self.end_of_line():
                return True
            
            return True
        
        return False

    def condition_block(self):
        # print("Entered condition block")
        
        if self.expression():
            self.symbol_table["IT"] = self.current_expression
            
            if self.symbol_table["IT"]:
                self.execute = True
            else:
                self.execute = False

            if self.end_of_line() and self.expect("O RLY?") and self.end_of_line() and self.expect("YA RLY") and self.end_of_line() and self.statements():
                self.execute = not self.execute

                if self.else_if_chain() and self.else_block() and self.expect("OIC") and self.end_of_line():
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
            self.current_variable = self.previous_token()
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

def DEBUG_SYMBOL_TABLE(symbol_table):
    print("\n\n\n------------SYMBOL TABLE-------------")
    
    for key, value in symbol_table.items():
        print(f"{key}\t\t\t{typecast_string(value)}")
    
    print("------------SYMBOL TABLE-------------\n\n\n")

def DEBUG_TOKENS(tokens):
    print("\n\n\n-----------TOKENS TABLE--------------")

    for token in tokens:
        print(f"{token[0]}\t\t\t{token[1]}")

    print("-----------TOKENS TABLE--------------\n\n\n")

def syntax_semantic_analyzer(tokens):
    analyzer = SyntaxSemanticAnalyzer(tokens)
    correct_program = analyzer.program()
    DEBUG_SYMBOL_TABLE(analyzer.symbol_table)
    return correct_program

def main():
    testcase = int(input())
    passed_all_test_cases = True
    test_cases_folder = Path("../../lolcode_test_cases")
    
    for file_path in sorted(test_cases_folder.glob("*.lol")):
        filename = file_path.name
        
        if int(filename[0:2]) != testcase:
            continue
        
        print(f"Processing file: {filename}")
        
        with open(file_path, "r") as file:
            code = file.read()
        
        print(code)
        tokens = lexical_analyzer(code)
        DEBUG_TOKENS(tokens)

        if not syntax_semantic_analyzer(tokens):
            passed_all_test_cases = False
            print(f"Failed at testcase: {filename}")
            break

    # if passed_all_test_cases:
        # print("Passed all test cases.")

if __name__ == "__main__":
    main()
