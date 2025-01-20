import sys


class IdentifyDataStructure:
    def __init__(self, line: str):
        print(line, file=sys.stderr, flush=True)
        self.structures = ['stack', 'queue', 'priority queue']
        self.data = dict((k, []) for k in self.structures)
        self.result = dict((k, True) for k in self.structures)
        self.process_line(line.split())
    
    def process_line(self, line: list):
        for el in line:
            if el[0] == 'i':
                self.push_element(el[1])
            elif el[0] == 'o':
                self.pop_element(el[1])

    def print_structures(self):
        return None

    def push_element(self, input_element: str):
        for key in self.data:
            self.data[key].append(input_element)

    def pop_element(self, output_element: str):
        element = None
        for key in self.data:
            if len(self.data[key]) == 0:
                self.result[key] = False
            elif key == 'stack':
                element = self.data[key].pop()
            elif key == 'queue':
                element = self.data[key].pop(0)
            elif key == 'priority queue':
                pq_max = self.data[key] 
                element = self.data[key].pop(pq_max.index(max(pq_max)))
            if element != output_element:
                self.result[key] = False

    def __repr__(self):
        score = sum(self.result.values())
        if score == 0:
            result = "mystery"
        elif score == 1:
            result = ""
            for key in self.result:
                if self.result[key]:
                    result = key
        else:
            result = "unsure"
        return f'{result}'


def main():
    n = int(input())
    for i in range(n):
        identify_line = IdentifyDataStructure(input())
        print(identify_line)
        print("", file=sys.stderr, flush=True)


if __name__ == '__main__':
    main()
