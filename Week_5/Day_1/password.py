username = input()
passwords_DB = input()

current_password = input()

while passwords_DB != current_password:
    current_password = input()

print(f"Welcome {username}!")