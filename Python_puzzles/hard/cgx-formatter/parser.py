def main():
    cgxline = "('users'=('admin'=('name'='toto';'age'=-42; 'password'='#0_tr) ='));('status'=true))"
    
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


if __name__ == "__main__":
    main()