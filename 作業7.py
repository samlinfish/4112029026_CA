# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:51:06 2023

@author: USER
"""

import re

class SimpleLexer(object):
    def _init_(self):
        self.token_rules = [
            ('NUMBER',   r'\d+'),
            ('PLUS',     r'\+'),
            ('MINUS',    r'-'),
            ('MULTIPLY', r'\*'),
            ('DIVIDE',   r'/'),
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('WS',       r'\s+'),
        ]
        self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_rules)
        self.re_token_regex = re.compile(self.token_regex)
        
    def tokenize(self, code):
        for mo in self.re_token_regex.finditer(code):
            kind = mo.lastgroup 
            value = mo.group()
            if kind == 'NUMBER':
                value = int(value)
            elif kind == 'WS':
                continue
            yield kind, value
            
code = '27 + (43 / 36 - 48) * 51'
lexer = SimpleLexer()
tokens = list(lexer.tokenize(code))
            
print(tokens)