import os

print("Checking ALL environment variables:")
print(f"MONGODB_USERNAME: {os.getenv('MONGODB_USERNAME')}")
print(f"MONGODB_PASSWORD: {os.getenv('MONGODB_PASSWORD')}") 
print(f"USRNM: {os.getenv('USRNM')}")
print(f"PASS: {os.getenv('PASS')}")

# Test if we can read them
username = os.getenv('MONGODB_USERNAME') or os.getenv('USRNM')
password = os.getenv('MONGODB_PASSWORD') or os.getenv('PASS')

print(f" Username found: {'Yes' if username else 'No'}")
print(f"Password found: {'Yes' if password else 'No'}")

if username and password:
    print("Credentials are available!")
else:
    print("No credentials found")