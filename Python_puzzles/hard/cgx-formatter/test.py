import sys
from cgx_formatter import Node, CgxLexerParser

def test_cgx_class(input):
    clp = CgxLexerParser(input)
    # output = clp.parse()

def test1to6():
    tests = {'1': "\\n\\n\\t true\\n\\n",
             '2': "'spaces and    tabs'",
             '3': "(0)",
             '4': "()",
             '5': "(0;1;2)",
             '6': "(('k1'=1);('k2'=2))"}

    for key, input in tests.items():
        print("test ", key, ":", input)
        test_cgx_class(key, input )
    # ans = "true"
    # print("test1", (res == ans * "[OK]" + (res != ans) * "** FAIL **" )
    # print("--" * 20)


def main():
    test1to6()


if __name__ == "__main__":
    main()