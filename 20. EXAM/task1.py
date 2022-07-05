from collections import deque

eggs = deque(input().split(', '))
papers = input().split(', ')

boxes_filled = 0

while eggs and papers:
    egg = int(eggs.popleft())
    if egg < 1:
        continue
    if egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue
    paper = int(papers.pop())

    if paper + egg <= 50:
        boxes_filled += 1

if boxes_filled == 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    print(f"Great! You filled {boxes_filled} boxes.")
if eggs:
        print(f'Eggs left: {", ".join(eggs)}')
if papers:
        print(f"Pieces of paper left: {', '.join(papers)}")
