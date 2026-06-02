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
        
usr1 = User('dylan','frank',22)
usr1.greet_user()
usr1.describe_user()