import json

# Load JSON data from the file
with open(r'C:\Users\marno\Wiley Edge\Code\Week 2\day2\jsonPractice.json', 'r') as file:
    data = json.load(file)

# Access and print information about each user
for user in data["users"]:
    print(f"User ID: {user['id']}")
    print(f"Username: {user['username']}")
    print(f"Email: {user['email']}")
    print()

# Filtering users by a specific condition 
target_email = "user2@example.com"
matching_users = [user for user in data["users"] if user["email"] == target_email]

if matching_users:
    print("Users with email", target_email)
    for user in matching_users:
        print(f"User ID: {user['id']}")
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
else:
    print("No users found with the email", target_email)
