import re


input_string = "some text before func(arg1, arg2) { function body } some text after"

pattern = r"(.*?)\bfunc\s*\((.*?)\)\s*{([^{}]*)}(.*?)"

match = re.match(pattern, input_string)

if match:
    before_func = match.group(1).strip()
    args = match.group(2).strip()
    body = match.group(3).strip()
    after_func = match.group(4).strip()

    print("Before func:", before_func)
    print("Args:", args)
    print("Body:", body)
    print("After func:", after_func)