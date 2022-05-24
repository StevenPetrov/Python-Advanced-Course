n, m = input().split()

n_set = set()
m_set = set()

for x in range(int(n)):
    num = int(input())
    n_set.add(num)
for x in range(int(m)):
    num = int(input())
    m_set.add(num)

unique = n_set & m_set

[print(x) for x in unique]