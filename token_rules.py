import re

patterns = [
    ("DATA_TYPE", r'\b(int|float|char|double|void)\b'),
    ("RELATIONAL_OPERATOR", r'==|!=|>=|<=|>|<'),
    ("LOGICAL_OPERATOR", r'&&|\|\||!'),
    ("FLOAT_CONSTANT", r'\b\d+\.\d+\b'),
    ("INTEGER_CONSTANT", r'\b\d+\b'),
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    ("DELIMITER", r'[;,(){}\[\]]'),
]

code = """
int total = 100;
float marks = 85.5;
if (total >= 50 && marks > 75.0) {
    total = total + 10;
}
"""

token_regex = '|'.join(
    f'(?P<T{i}>{pattern})'
    for i, (_, pattern) in enumerate(patterns)
)

print("INPUT CODE:")
print(code)

print("\nTOKEN OUTPUT:")
for match in re.finditer(token_regex, code):
    token_type = int(match.lastgroup[1:])
    name = patterns[token_type][0]
    print(f"{match.group():<15} -> {name}")