from json import dumps,loads


def register(username, password):
    with open('./users.txt', 'r') as users_db:
        for line in users_db:
            user = loads(line.strip())
            if user['username'] == username:
                return False
    with open('./users.txt', 'a') as users_db:
        user = {
            'username': username,
            'password': password,
        }
        user_json = dumps(user)
        users_db.write(user_json + '\n')
        return True


def login(username, password):
    with open('./users.txt', 'r') as users_db:
        for line in users_db:
            user = loads(line.strip())
            if user['username'] == username and user['password'] == password:
                return True
        return False
