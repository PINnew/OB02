class User():

    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f'Пользователь успешно добавлен в список')
        print('user_list')

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(user_list)


users = []
admin = Admin('a1', 'Gocha')
user1 = User('u1', 'Stepa')
user2 = User('u2', 'Lena')
user3 = User('u3', 'Tota')

print('\nСписок user')
for user in users:
    print(user)

print(user1.get_name(), user1.get_user_id(), user1.get_level())
print(user2.get_name(), user2.get_user_id(), user2.get_level())
print(user3.get_name(), user3.get_user_id(), user3.get_level())

print('\nСписок admin')
for admin in users:
    print(admin)

print(admin.get_name(), admin.get_user_id(), admin.get_level())
