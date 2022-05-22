left = list()

string = input()
triggered = False
for x in string:
    if x == '(':
        left.append(1)
    elif x == '{':
        left.append(2)
    elif x == '[':
        left.append(3)
    else:
        if left:
            if x == ')' and left[-1] == 1:
                left.pop()
            elif x == '}' and left[-1] == 2:
                left.pop()
            elif x == ']' and left[-1] == 3:
                left.pop()
            else:
                triggered = True
        else:
            triggered = True
if left:
    triggered = True

if not triggered:
    print('YES')
else:
    print('NO')