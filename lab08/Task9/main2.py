from User import User
from admin_module import Admin

user1 = User("Олександр", "Іваненко", "alex@example.com", "Alex")
user2 = User("Марія", "Петренко", "maria@example.com", "Maria")
user3 = User("Ігор", "Коваль", "igor@example.com", "Igor")

for user in [user1, user2, user3]:
    print(user.describe_user())
    print(user.greeting_user())
    print('\n')

test_user = User("Тест", "Користувач", "test@example.com", "Tester")
print(test_user.increment_login_attempts())
print(test_user.increment_login_attempts())
print(test_user.increment_login_attempts())
print(test_user.reset_login_attempts())

admin_user = Admin("Адмін", "Системний", "admin@example.com", "Admin")
print(admin_user.describe_user())
print(admin_user.greeting_user())

print(admin_user.priv.show_privileges())
