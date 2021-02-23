class Player:
    # this is a static variable
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1

    # mark method as static method
    @staticmethod
    def get_count():
        return Player.count


sanga = Player('Sanga')
mahela = Player('Mahela')

print(sanga.count)
print(mahela.count)
print(sanga.count)

# Since this is a static method, it will not automatically add self when it calling
print(Player.get_count())

# Note: Don't try to set static variable like below.Then it act as a instance variable(since python in dynamic)
# sanga.count=5

# If you want to set static variable values, use below syntax
# Player.count = 5
