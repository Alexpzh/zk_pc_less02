users = []

class User():
    def __init__(self, id, name, level = 'user'):
        self.__id = id
        self.__name = name
        self.__level = level

    def get_id(self):
        return self.__id

    def set_id(self, val_id):
        self.__id = val_id

    def get_name(self):
        return self.__name

    def set_name(self, val_name):
        self.__name = val_name

    def get_level(self):
        return self.__level

    def set_level(self, val_level):
        self.__level = val_level

    def user_info(self):
        print('Id=',self.__id,'\tName=', self.__name, '\tLevel=', self.__level)
        # print('Name=', self.__name)
        # print('Level=', self.__level)

class Admin(User):
    def __init__(self,id, name, level = 'admin'):
        super().__init__(id, name)
        self.set_level('admin')

    def add_user(self, user_name):
        if self._User__level != 'admin':
            return

        id = 0;
        for user in users:
            if user.get_id() > id:
                id = user.get_id()
        id +=1
        val_user = User(id, user_name)
        users.append(val_user)

    def remove_user(self, user_name):
        if self._User__level != 'admin':
            return
        for user in users:
            if user.get_name() == user_name:
                users.remove(user)

admin1 = Admin(0, 'Boss')
print('Admin created')
admin1.user_info()

print('\nAdd users:\n')
admin1.add_user('Petya')
admin1.add_user('Vasia')
admin1.add_user('Olya')
admin1.add_user('Masha')

for user in users:
    user.user_info()

print('\nRemove user Petya:')
admin1.remove_user('Petya')
print('\nList users:\n')
for user in users:
    user.user_info()




