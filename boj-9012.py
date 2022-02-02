for i in range(int(input())):
    stack = []
    isVPS = True
    for bracket in input():
        if bracket == "(":
            stack.append(bracket)
        else:
            if stack:
                stack.pop()
            else:
                isVPS = False
                break
    if stack:
        isVPS = False
    print("YES" if isVPS else "NO")
