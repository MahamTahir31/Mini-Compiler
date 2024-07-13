# LANGUAGE : CEEPY (LEXICAL ANALYZER)
# __
import re
import pandas as pd

keyword_classes = {
    'int': 'DT',
    'float': 'DT',
    'char': 'DT',
    'str': 'DT',
    'bool': 'DT',
    'if': 'If',
    'elif': 'Elif',
    'default': 'Default',
    'for': 'For',
    'continue': 'BreakCon',
    'break': 'BreakCon',
    'return': 'Return',
    'main': 'Main',
    'klass': 'Class',
    'secure': 'AccessMod',
    'public': 'AccessMod',
    'self': 'Self',
    'static': 'Static',
    'func': 'Func',
    'virtual': 'Virtual',
    'void': 'Void',
    'new': 'New'
}

punctuator_classes = {
    ';': ';',
    ',': ',',
    '(': '(',
    ')': ')',
    '{': '{',
    '}': '}',
    '.': '.',
    '[': '[',
    ']': ']',
    '-:': '-:',
    '=>': '=>',
    '::': '::',
    ':': ':'
}

operator_classes = {
    '+': 'PM',
    '-': 'PM',
    '*': 'PMDM',
    '/': 'PMDM',
    '%': 'PMDM',
    '^': 'PMDM',
    '++': 'inc_dec',
    '--': 'inc_dec',
    '!': 'Not',
    '=': '=',
    '==': 'RO',
    '<': 'RO',
    '>': 'RO',
    '<=': 'RO',
    '>=': 'RO',
    '!=': 'RO',
    '&&': 'AND',
    '||': 'OR_op',
    '+=': 'OP_assign',
    '-=': 'OP_assign',
    '/=': 'OP_assign',
    '*=': 'OP_assign',
    '%=': 'OP_assign'
}

# Updated identifier pattern based on provided rules
identifier_pattern = r'\$[a-zA-Z][a-zA-Z0-9_]*'
# identifier_pattern = r'\$[a-zA-Z][a-zA-Z0-9_](?:\([^)]\))?'

# Bool Constants
bool_const = ['True', 'False']
# bool_const = ['true', 'false']

# Regular Expression for integer constants
int_const_pattern = r'-?(0|[1-9]\d*)(?:\.\d+)?'

# Updated regular expression for matching float constants

float_const_pattern = r'-?(\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'

# Updated regular expression for matching character constants
char_constant_pattern = r"'(?:[^'\\]|\\.)'"

# Regular expression for matching string constants
string_constant_pattern = r'"(?:\\.|[^"\\])*"'

# Regular expression for matching spaces, punctuators, and operators
delimiter_pattern = r'\s+|' + '|'.join(re.escape(op) for op in operator_classes.keys()) + '|' + '|'.join(re.escape(punc) for punc in punctuator_classes.keys())



# Regular expression for matching operators that are two characters in length
two_char_operators_pattern = '|'.join(re.escape(op) for op in operator_classes.keys() if len(op) == 2)

# Regular expression for matching punctuators that are two characters in length
two_char_punctuators_pattern = '|'.join(re.escape(punc) for punc in punctuator_classes.keys() if len(punc) == 2)

# Modify the token pattern for keywords
keyword_pattern = r'\b(?:' + '|'.join(re.escape(keyword) for keyword in keyword_classes.keys()) + r')\b'

# Patterns for constants
int_const_pattern = r'-?(0|[1-9]\d*)(?:\.\d+)?'

float_const_pattern = r'-?(?:\d+\.\d+|\.\d*)(?:[eE][-+]?\d+)?|\.\d+(?:[eE][-+]?\d+)?'

char_constant_pattern = r"'(?:[^'\\]|\\.)'"
string_constant_pattern = r'"(?:\\.|[^"\\])*"'


# Regular expression for matching operators and punctuators
operator_pattern = '|'.join(re.escape(op) for op in operator_classes.keys())
punctuator_pattern = '|'.join(re.escape(punc) for punc in punctuator_classes.keys())


combined_pattern = (
    f'{float_const_pattern}|{int_const_pattern}|{char_constant_pattern}|'
    f'{two_char_punctuators_pattern}|{two_char_operators_pattern}|'
    f'{string_constant_pattern}|{keyword_pattern}|{operator_pattern}|'
    f'{punctuator_pattern}|{identifier_pattern}|[^ \t\n]+'
)

token_patterns = [
    (combined_pattern, 'TOKEN'),
]
    
def is_valid_char_constant(constant):
    with_backslash_pattern = r"\\[ntrbo'\"\\]"
    if re.match(with_backslash_pattern, constant):
        return len(constant) == 4
    without_backslash_pattern = r"[^'\"\\]"
    if re.match(without_backslash_pattern, constant):
        return len(constant) == 3
    return False

def tokenize(code):

    
    code = re.sub(r'(?<=\w);', ' ;', code)

    code = re.sub(r'(?<=\w)\(', ' (', code)
    

    tokens = []
    lines = code.split('\n')
    line_number = 0

    inside_multiline_comment = False

    for line in lines:
        line_number += 1

        # Check for multi-line comment start and end
        if '<-' in line:
            inside_multiline_comment = True
            if '->' in line:
                inside_multiline_comment = False
            continue
        elif '->' in line:
            inside_multiline_comment = False
            continue

        # Skip lines starting with ~~ (single-line comments)
        if line.startswith('~~'):
            continue

        if inside_multiline_comment:
            continue  # Skip lines inside multi-line comments

        matches = re.finditer(token_patterns[0][0], line)
        matched = False

        for match in matches:
            token_value = match.group(0)
            token_type = 'Invalid Lexeme'

            # Check if token_value is a standalone dot
            if token_value == '.':
                token_type = '.'  # Treat standalone dot as a separate token
                tokens.append([token_type, token_value, line_number])
                matched = True
                continue

            if re.match(float_const_pattern, token_value):
                token_type = 'float_const'
                
            elif re.match(int_const_pattern, token_value):
                token_type = 'int_const'
            # Check if token_value is of the form 'b.98'
            elif re.match(r'\w+\.\d+', token_value):
                # Split the token_value into two tokens: 'b' and '.98'
                var, num = token_value.split('.')
                tokens.append(['Invalid Lexeme', var, line_number])  # Add 'b' as 'ID'
                tokens.append(['float_const', '.' + num, line_number])  # Add '.98' as 'float_const'
                matched = True
                continue

            elif re.match(char_constant_pattern, token_value):
                token_type = 'char_const'
                token_value = token_value[1:-1]  # strip the single quotes
                if token_value == '\\\\':  # check for escaped backslash
                    token_value = '\\'  # convert to single backslash

            elif re.match(string_constant_pattern, token_value):
                token_type = 'str_const'
                token_value = token_value[1:-1]  # strip the double quotes

                
        
            # elif re.match(string_constant_pattern, token_value):
            #     token_type = 'string_const'
            
            elif re.match(identifier_pattern, token_value):
                token_type = 'ID'
            elif re.match(keyword_pattern, token_value):
                token_type = keyword_classes[token_value]
            elif token_value in operator_classes:
                token_type = operator_classes[token_value]
 
        
            elif token_value in punctuator_classes:
                token_type = punctuator_classes[token_value]
            elif token_value in bool_const:
                token_type = 'bool_const'

            tokens.append([token_type, token_value, line_number])
            matched = True

        if not matched:
            invalid_lexemes = line.split()
            for invalid_lexeme in invalid_lexemes:
                tokens.append(['Invalid Lexeme', invalid_lexeme, line_number])

    return tokens

def main():
    input_file_name = "input.txt"
    output_file_name = "output.txt"

    try:
        with open(input_file_name, 'r') as input_file:
            source_code = input_file.read()
    except FileNotFoundError:
        print(f"Error: {input_file_name} not found.")
        return

    tokens = tokenize(source_code)

    try:
        with open(output_file_name, 'w') as output_file:
            for token_type, token_value, line_number in tokens:
                output_file.write(f"{token_type}, {token_value}, Line {line_number}\n")

            # Add the end marker token
            output_file.write("@, @, Line -1\n")

    except IOError:
        print(f"Error writing to {output_file_name}.")
    else:
        print(f"Tokens have been written to {output_file_name} file.")

    tokens = tokenize(source_code)

    data = []
    for token_type, token_value, line_number in tokens:
        data.append({'Class': token_type, 'Value': token_value, 'Line': line_number})

    data.append({'Class': '@', 'Value': '@', 'Line': -1})

    df = pd.DataFrame(data)
    print(df.to_string(index=False))

if __name__ == '__main__':
    main()