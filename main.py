import re


def tokenize(args: str) -> str:
    args = fr"{args}"
    args = re.sub("\n", "", args)
    args = re.sub(" ", "", args)
    args = re.split("\{*\}+$", args)
    return args


deepString: str = '''
func {this}
'''

if __name__ == '__main__':
    print(tokenize(deepString))
