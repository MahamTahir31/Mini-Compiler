# LANGUAGE : CEEPY ( LEXICAL ANALYZER)
# ____________________________________
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
    '*': 'MDM',
    '/': 'MDM',
    '%': 'MDM',
    '^': 'P',
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

# Bool Constant
bool_const = ['True', 'False']

# Regular Expression for integer constant
int_const_pattern = r'-?(?!0\d)\d+'

# Updated regular expression for matching float constants
float_const_pattern = r'-?(?:\d+\.\d+|\.\d*)(?:[eE][-+]?\d+)?|\.\d+(?:[eE][-+]?\d+)?'
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

token_patterns = [
    (r'(?<!\w)' + float_const_pattern + r'(?!\w)', 'float_const'),
    (r'(?<!\w)' + int_const_pattern + r'(?!\w)', 'int_const'),
    (char_constant_pattern, 'char_const'),
    (string_constant_pattern, 'str_const'),
    (keyword_pattern, 'KEYWORD'),  # Modify this line to use the keyword_pattern
    (r'\b(?:' + '|'.join(re.escape(boolean) for boolean in bool_const) + r')\b', 'bool_const'),
    (two_char_operators_pattern, 'OPERATOR'),
    (two_char_punctuators_pattern, 'PUNCTUATOR'),
    (r'|'.join(re.escape(punc) for punc in punctuator_classes.keys() if len(punc) == 1), 'PUNCTUATOR'),
    (r'|'.join(re.escape(op) for op in operator_classes.keys() if len(op) == 1), 'OPERATOR'),
    (identifier_pattern, 'ID'),
    (r'[^ \t\n]+', 'Invalid Lexeme'),
]


def is_valid_char_constant(constant):
    # Match character constants with a backslash
    with_backslash_pattern = r"\\[ntrbo'\"\\]"
    if re.match(with_backslash_pattern, constant):
        return len(constant) == 4

    # Match character constants without a backslash
    without_backslash_pattern = r"[^'\"\\]"
    if re.match(without_backslash_pattern, constant):
        return len(constant) == 3
    return False

def tokenize(code):
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

        combined_pattern = '|'.join(f'({pattern})' for pattern, _ in token_patterns)

        matches = re.finditer(combined_pattern, line)
        matched = False

        for match in matches:
            for idx, (pattern, token_type) in enumerate(token_patterns):
                if match.group(idx + 1):
                    matched = True
                    token_value = match.group(0)

                    if pattern == char_constant_pattern or is_valid_char_constant(token_value):
                        
                        tokens.append([token_type, token_value, line_number])
                    elif token_value in punctuator_classes:
                        token_type = punctuator_classes[token_value]
                        tokens.append([token_type, token_value, line_number])
                    elif token_value in operator_classes:
                        token_type = operator_classes[token_value]
                        tokens.append([token_type, token_value, line_number])
                    elif re.match(identifier_pattern, token_value):
                        token_type = 'ID'
                        tokens.append([token_type, token_value, line_number])
                    elif re.match(float_const_pattern, token_value):
                        token_type = 'float_const'
                        tokens.append([token_type, token_value, line_number])
                    elif re.match(int_const_pattern, token_value):
                        token_type = 'int_const'
                        tokens.append([token_type, token_value, line_number])
                    elif is_valid_char_constant(token_value):
                        token_type = 'char_const'
                        tokens.append([token_type, token_value, line_number])
                    elif re.match(string_constant_pattern, token_value):
                        string_value = token_value[1:-1]
                        tokens.append([token_type, string_value, line_number])
                    elif token_value in bool_const:
                        token_type = 'bool_const'
                        tokens.append([token_type, token_value, line_number])
                    elif token_value in keyword_classes:
                        token_type = keyword_classes[token_value]
                        tokens.append([token_type, token_value, line_number])
                    else:
                        tokens.append(['Invalid Lexeme', token_value, line_number])  # Handle invalid lexemes
                    break  # Break once a pattern is matched

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

            # Add the end marker tokenv
            output_file.write("@, @, Line -1\n")  # You can use -1 for the line number

    except IOError:
        print(f"Error writing to {output_file_name}.")
    else:
        print(f"Tokens have been written to {output_file_name} file.")

    tokens = tokenize(source_code)

    data = []
    for token_type, token_value, line_number in tokens:
        data.append({'Class': token_type, 'Value': token_value, 'Line': line_number})
        

    # Add the end marker token to the data
    data.append({'Class': '@', 'Value': '@', 'Line': -1})  # You can use -1 for the line number

    df = pd.DataFrame(data)
    print(df.to_string(index=False))

if __name__ == '__main__':
    main()

