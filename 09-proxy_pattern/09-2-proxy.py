
class SensitiveInfo(object):

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), " ".join(self.users)))

    def add(self, user):
        self.users.append(user)
        print("Added user: ", user)


class Info(object):
    """
    SensitiveInfo的保护代理
    """
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '123'

    def read(self):
        """读取用户不需要权限限制"""
        self.protected.read()

    def add(self, user):
        """添加权限限制"""
        sec = input("What is the secret?")
        self.protected.add(user) if sec == self.secret else print("Secret Wrong!")


def main():
    info = Info()
    while True:
        print("1 查看用户 \n2 添加用户 \n3 退出")
        key = input("choose number to option: ")
        if key == '1':
            info.read()
        elif key == '2':
            name = input("Choose username:")
            info.add(name)
        elif key == '3':
            exit()
        else:
            print("Unknow option:", key)


if __name__ == '__main__':
    main()
