import re


def tokenize(args: str) -> str:
    args = fr"{args}"
    args = re.sub("\n", "", args)
    args = re.sub(" ", "", args)
    args = re.split("(func|}$|)", args)
    return args


deepString: str = '''
Y:svar = 2;
func main(){
int = 5;
printf("The number is %k", X);
}
Z:svar = 3;
A:svar = 7;
'''

if __name__ == '__main__':
    print(tokenize(deepString))
