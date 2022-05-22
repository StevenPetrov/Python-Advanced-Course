from collections import deque

# clients = []
#
# while True:
#     command = input()
#     if command == "End":
#         break
#     if command == 'Paid':
#         for x in clients:
#             print(x)
#             clients = []
#     else:
#         clients.append(command)
# print(f"{len(clients)} people remaining.")

clients = deque()

while True:
    command = input()
    if command == "End":
        break
    if command == 'Paid':
        while clients:
            print(clients.popleft())
    else:
        clients.append(command)
print(f"{len(clients)} people remaining.")
