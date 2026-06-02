class User:
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def describe_user(self):
        print(f'用户的姓名是 {self.first_name.title()} {self.last_name.title()}')
        print(f'用户的年龄是 {self.age} 岁')

    def greet_user(self):
        print(f'Hello! Welcome aboard, {self.first_name.title()} '
              f'{self.last_name.title()}!')

class Admin(User):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)
        self.privileges = ['can add post', 'can delete post','can ban user']

    def show_privileges(self):
        print('管理员有如下的权限：')
        for item in self.privileges:
            print(f'\t{item}')

admin1= Admin('Lux','Demacia',18)
admin1.show_privileges()