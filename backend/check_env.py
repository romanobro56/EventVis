import os
from dotenv import load_dotenv

load_dotenv()

def check_environment():
    print(" Checking Environment Variables...")
    
    username = os.getenv('USRNM')
    password = os.getenv('PASS')
    
    print(f"USRNM: {'Set' if username else 'NOT SET'}")
    print(f"PASS: {'Set' if password else 'NOT SET'}")
    
    if username and password:
        print("Environment variables are properly configured!")
        # Show a masked version of the credentials
        masked_username = username[:3] + '***' + username[-2:] if len(username) > 5 else '***'
        masked_password = '******'
        print(f"Username: {masked_username}")
        print(f"Password: {masked_password}")
    else:
        print("\nTo set environment variables:")
        print("1. Create a backend/.env file with:")
        print("   USRNM=your_username")
        print("   PASS=your_password")
        print("2. OR set system environment variables USRNM and PASS")
    
    return bool(username and password)

if __name__ == "__main__":
    check_environment()