import asyncio
import aiohttp
import os
import webbrowser
from datetime import datetime

def print_ascii_art():
    print("\033[91m")
    print(" ██▒   █▓ █    ██  ▄▄▄█████▓ ██░ ██  ▓█████  ██▀███   ▓█████     ▄████▄   ▒█████   ███▄ ▄███▓")
    print("▓██░   █▒ ██  ▓██▒▓  ██▒ ▓▒▓██░ ██▒ ▓█   ▀ ▓██ ▒ ██▒ ▓█   ▀    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒")
    print(" ▓██  █▒░▓██  ▒██░▒ ▓██░ ▒░▒██▀▀██░ ▒███   ▓██ ░▄█ ▒ ▒███      ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░")
    print("  ▒██ █░░▓▓█  ░██░░ ▓██▓ ░ ░▓█ ░██  ▒▓█  ▄ ▒██▀▀█▄   ▒▓█  ▄    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ")
    print("   ▒▀█░  ▒▒█████▓   ▒██▒ ░ ░▓█▒░██▓ ░▒████▒░██▓ ▒██▒ ░▒████▒   ▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒")
    print("   ░ ▐░  ░▒▓▒ ▒ ▒   ▒ ░░    ▒ ░░▒░▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ░░ ▒░ ░   ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░")
    print("   ░ ░░  ░░▒░ ░ ░     ░     ▒ ░▒░ ░  ░ ░  ░  ░▒ ░ ▒░  ░ ░  ░     ░  ▒     ░ ▒ ▒░ ░  ░      ░")
    print("     ░░   ░░░ ░ ░   ░       ░  ░░ ░    ░     ░░   ░     ░      ░        ░ ░ ░ ▒  ░      ░   ")
    print("      ░     ░               ░  ░  ░    ░  ░   ░         ░  ░   ░ ░          ░ ░         ░   ")
    print("     ░                                                      ░                                ")
    print("\033[0m")
    print("                         <= Made by:Vuthere =>")
    print("Github:                  github.com/Vuthere")
    print("Discord:                 dc.vuthere.com")
    print("This program will fetch and save your Discord user data to a file.\n")

async def fetch_and_save_user_data(user_token):
    headers = {
        "Authorization": user_token,
        "Content-Type": "application/json"
    }
    
    data_to_save = {}
    async with aiohttp.ClientSession() as session:
        async with session.get("https://canary.discordapp.com/api/v9/users/@me", headers=headers) as response:
            if response.status == 200:
                user_info = await response.json()
                banner_url = f"https://cdn.discordapp.com/banners/{user_info.get('id')}/{user_info.get('banner')}.png" if user_info.get('banner') else "Not available"
                premium_type = "Nitro Classic" if user_info.get('premium_type') == 2 else "Nitro Boost" if user_info.get('premium_type') == 1 else "No Nitro"
                data_to_save['user'] = {
                    "username": user_info.get('username', ''),
                    "avatar_url": f"https://cdn.discordapp.com/avatars/{user_info.get('id')}/{user_info.get('avatar')}.png",
                    "banner_url": banner_url,
                    "discriminator": user_info.get('discriminator', ''),
                    "id": user_info.get('id', ''),
                    "email": user_info.get('email', 'Not available'),
                    "phone": user_info.get('phone', 'Not available'),
                    "mfa_enabled": user_info.get('mfa_enabled', 'Not available'),
                    "locale": user_info.get('locale', 'Not available'),
                    "verified": user_info.get('verified', 'Not available'),
                    "flags": user_info.get('flags', 'Not available'),
                    "premium_type": premium_type,
                }
                filename = f"{user_info.get('username', 'user').replace(' ', '_').lower()}-{datetime.now().strftime('%Y_%m_%d')}.data.yml"
                with open(filename, 'w') as file:
                    file.write(str(data_to_save))  
                print(f"Data saved to {filename}")
            else:
                print("[ERROR] Your token might be invalid. Please check it again.")

async def main_menu():
    webbrowser.open("https://dc.vuthere.com")
    os.system('cls' if os.name == 'nt' else 'clear')  
    print_ascii_art()  
    user_token = input("Please enter your Discord token: ")
    os.system('cls' if os.name == 'nt' else 'clear')  
    
    if not user_token:
        print("[ERROR] Token is missing.")
        return
    
    while True:
        print_ascii_art()  
        print("\n1. Fetch and Save User Data")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            await fetch_and_save_user_data(user_token)
            print("\nPress Enter to continue...")
            input()  
            os.system('cls' if os.name == 'nt' else 'clear')  
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid input, please enter 1 or 2.")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    asyncio.run(main_menu())