word = input()

stacks = []
count = -1
for x in word:
    count += 1
    if x == "(":
        stacks.append(count)
    elif x == ")":
        last = stacks.pop()
        print(word[last:count + 1])
