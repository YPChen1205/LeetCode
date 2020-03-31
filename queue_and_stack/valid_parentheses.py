
def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for i in s:
        if i == "(":
            stack.append(')')
        if i == "[":
            stack.append(']')
        if i == "{":
            stack.append("}")
        if i == "}" or i == ")" or i == "]":
            if stack[-1] == i:
                stack.pop()
            else:
                return False
    if not stack:
        return True

if __name__ == '__main__':
    print(is_valid('(}'))
    print(is_valid('([)]'))
    print(is_valid('{[]}'))