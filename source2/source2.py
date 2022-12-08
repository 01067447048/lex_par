from enum import Enum, auto

class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    SEMICOLON = auto()
    COLON = auto()

    COMMA = auto()
    DOT = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    MODULAR = auto()

    EQUAL = auto()
    EQUAL_EQUAL = auto()
    EXCLAM = auto()
    EXCLAM_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()

    IDENTIFIER = auto()

    BOOLEAN = auto()
    NUMBER = auto()
    SINGLE_STRING = auto()
    DOUBLE_STRING = auto()

    EOF = auto()
    UNKNOWN = auto()
    TAB = '\t'

    IF = 'if'
    ELSE = 'else'
    AND = 'and'
    OR = 'or'
    FUN = 'def'
    VAR = 'var'
    TRUE = 'true'
    FALSE = 'false'
    NULL = 'null'
    FOR = 'for'
    WHILE = 'while'
    IN = 'in'
    RETURN = 'return'
    SWITCH = 'switch'
    CASE = 'case'
    BREAK = 'break'
    CONTINUE = 'continue'
    NEW = 'new'
    CLASS = 'class'
    INTERFACE = 'interface'
    EXTEND = 'extend'
    IMPLEMENT = 'implement'
    PACKAGE = 'package'
    IMPORT = 'import'
    NOT = 'not'
    # PRINT = 'print'

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)