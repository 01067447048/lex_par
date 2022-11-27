from .token import Token
from typing import List

class Embedder:
    def __init__(self):
        self.embedding_dict: dict = {
            "PLUS": 0,
            "MINUS": 1,
            "STAR": 2,
            "SLASH": 3,
            "MODULAR": 4,
            "EQUAL": 5,
            "EQUAL_EQUAL": 6,
            "EXCLAM": 7,
            "EXCLAM_EQUAL": 8,
            "GREATER": 9,
            "GREATER_EQUAL": 10,
            "LESS": 11,
            "LESS_EQUAL": 12,
            "LEFT_PAREN": 13,
            "RIGHT_PAREN": 14,
            "LEFT_BRACE": 15,
            "RIGHT_BRACE": 16,
            "LEFT_BRACKET": 17,
            "RIGHT_BRACKET": 18,
            "SEMICOLON": 19,
            "COLON": 20,
            "COMMA": 21,
            "DOT": 22,
            "IDENTIFIER": 23,
            "BOOLEAN": 24,
            "NUMBER": 25,
            "SINGLE_STRING": 26,
            "DOUBLE_STRING": 27,
            "IF": 28,
            "ELSE": 29,
            "AND": 30,
            "OR": 31,
            "FUN": 32,
            "VAR": 33,
            "TRUE": 34,
            "FALSE": 35,
            "NULL": 36,
            "FOR": 37,
            "WHILE": 38,
            "IN": 39,
            "RETURN": 40,
            "SWITCH": 41,
            "CASE": 42,
            "BREAK": 43,
            "CONTINUE": 44,
            "NEW": 45,
            "CLASS": 46,
            "INTERFACE": 47,
            "EXTEND": 48,
            "IMPLEMENT": 49,
            "UNKNOWN": 50,
            "PACKAGE": 51,
            "IMPORT": 52,
            "NOT": 7,
            "TAB": 53,
            "EOF": 99
        }

    def get_embedding(self, tokens: List) -> List:
        return_list = []
        for token in tokens:
            return_list.append(self.embedding_dict[token.type.name])

        return return_list