def print_user_data(username, password, email=None, age=None, address=None):
    print(f"Username: {username}")
    print(f"Password: {password}")

    print(f"Address: {address}")
    print(f"Email: {email}")
    print(f"Age: {age}")


print_user_data(
    email="robert@gmail.com",
    username="robert",
    age=30,
    password="testpas123",
    address="Budapest"
)

print_user_data("robert", "testpas123", "Budapest", "robert@gmail.com", 30)