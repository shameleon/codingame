import sys
import math

""" progress 100% """


class MimeMap:
    def __init__(self, n):
        """input : ext file extension
                   mt: MIME type. """
        mime_ext = []
        mime_types = []
        for i in range(n):
            ext, mt = input().split()
            print("INPUT", ext, mt, file=sys.stderr, flush=True)
            mime_ext.append(ext.lower())
            mime_types.append(mt)
        self.map = dict(zip(mime_ext, mime_types))

    def get_mime_type(self, line):
        """ For each of the Q filenames, display on a line
         the corresponding MIME type. If there is no corresponding type, 
         then display UNKNOWN. """
        print("     fname", line, file=sys.stderr, flush=True)
        d = line.rfind('.')
        if d == -1:
            print("UNKNOWN")
            return
        extension = line[d + 1:].lower()
        if extension in self.map.keys():
                print(self.map[extension])
                return
        print("UNKNOWN")
        return


if __name__ == "__main__":
    n = int(input())  # Number of elements which make up the association table.
    q = int(input())  # Number Q of file names to be analyzed.
    mime = MimeMap(n)
    for i in range(q):
        fname = input()  # One file name per line.
        mime.get_mime_type(fname)

