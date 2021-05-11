from collections import defaultdict


class IpInfoWriter:

    def __init__(self):
        self._info = defaultdict(list)

    def append(self, data):
        for key, value in data.items():
            self._info[key].append(repr(value))

    def write(self):
        with open('results.txt','w') as out:
            for key, value in self._info.items():
                lines = []
                [lines.append(line) for line in value]
                lines.append(160*"=")
                lines.append("\n")
                out.writelines(lines)


