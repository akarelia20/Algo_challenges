def solution(string, markers):
    newlines = []
    lines = string.splitlines()
    for line in lines:
        new_str = line
        for marker in markers:
            idx = new_str.find(marker)
            if (idx != -1):
                new_str = new_str[:idx]
        newlines.append(new_str.rstrip())
    return '\n'.join(newlines)
