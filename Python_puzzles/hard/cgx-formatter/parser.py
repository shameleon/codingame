
def draw_line(cgxline):
    blocks = 0
    primitive = False
    b = ""
    p = ""
    sep = ""
    for ch in cgxline:
        if ch == '\'':
            primitive = not primitive
        if not primitive:
            blocks += (ch == '(')
            blocks -= (ch == ')')
        b += str(blocks)
        p += " " * (not primitive) + "-" * primitive
        if ch in [';', '='] and not primitive:
            sep += "|"
        else:
            sep += " "
    print(cgxline)
    print(b)
    print(p)
    print(sep)

    for ch in cgxline:
        if ch == '\'':
            is_in_primitive = not is_in_primitive


def is_block(line):
    if line[-1] == ';':
        line = line[0:-1]
    if line[0] == '(' and line[-1] == ')':
        primitive = False

    return line


def print_token(self, token: str, indent: int, next_elem: bool, elem_type='Default'):
    str = (" " * 4 * indent) + token + next_elem * ";"
    endline = '\n'
    print(str, end=endline)


def main():
    cgxline = "('users'=('admin'=('name'='toto';'age'=-42; 'password'='#0_tr) ='));('status'=true))"
    draw_line(cgxline)
    indent_level = 0
    in_primitive = False
    line = ""
    for ch in cgxline:
        if ch == '\'':
            primitive = not primitive
            if ch == '\'' and not primitive:
                line += ch
            print_token('(', indent_level, False)
        if ch == '(' and not primitive:
            print_token('(', indent_level, False)
            indent_level += 1
        elif ch == ')' and not primitive:
            indent_level -= 1
            print_token(')', indent_level, False)


if __name__ == "__main__":
    main()