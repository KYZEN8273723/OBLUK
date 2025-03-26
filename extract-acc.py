import os
import requests
import uuid
import random
from rich.console import Console
from rich.panel import Panel

# Console Setup
console = Console()

# Define color codes
green = '[bold green]'
red = '[bold red]'
reset = '[bold white]'

folder_name = "/sdcard/Test"
file_names = ["toka.txt", "tokaid.txt", "tokp.txt", "tokpid.txt", "cok.txt", "cokid.txt"]

# Check if folder exists
if not os.path.exists(folder_name):
    try:
        os.makedirs(folder_name)
        console.print(Panel(f"📁 Folder '{folder_name}' created successfully!", style="green"))
    except Exception as e:
        console.print(Panel(f"❌ Failed to create folder '{folder_name}': {e}", style="red"))
else:
    console.print(Panel(f"📂 Folder '{folder_name}' already exists.", style="blue"))

# Check if files exist
for file_name in file_names:
    file_path = os.path.join(folder_name, file_name)
    if not os.path.exists(file_path):  
        try:
            with open(file_path, 'w') as file:
                pass  
            console.print(Panel(f"✅ File '{file_path}' created.", style="green"))
        except Exception as e:
            console.print(Panel(f"❌ Failed to create file '{file_path}': {e}", style="red"))
    else:
        console.print(Panel(f"📄 File '{file_path}' already exists.", style="blue"))

# Line Separator
def linex():
    console.print(Panel("━" * 50, style="cyan"))

# Count Lines in a File
def count_lines(filepath):
    try:
        if os.path.exists(filepath):
            with open(filepath, 'r') as file:
                return sum(1 for _ in file)
        else:
            return 0
    except Exception as e:
        console.print(Panel(f"❌ Error counting lines in {filepath}: {e}", style="red"))
        return 0

# Overview Panel
def overview():
    linex()
    total_accounts = count_lines("/sdcard/Test/toka.txt")
    total_pages = count_lines("/sdcard/Test/tokp.txt")
    console.print(Panel(f"📊 [bold yellow]OVERVIEW[/bold yellow]\n\n"
                        f"🟢 TOTAL ACCOUNTS: {total_accounts}\n🔵 TOTAL PAGES: {total_pages}",
                        style="magenta"))

# Main Menu
def Initialize():
    console.print(Panel("[bold cyan]Choose how you want to extract:[/bold cyan]\n\n"
                        "[1] Manual through Input\n"
                        "[2] Manual through File\n"
                        "[3] Automatic through File\n"
                        "[4] Overview",
                        title="[bold yellow]🔥 BOOSTING PANEL 🔥[/bold yellow]", style="blue"))

    choice = input("\n➡️ Choose: ")
    if choice == '1':
        Manual()
    elif choice == '2':
        ManFile()
    elif choice == '3':
        Auto()
    elif choice == '4':
        overview()
    else:
        console.print(Panel("❌ Invalid option. Try again!", style="red"))
        Initialize()

# Manual Input
def Manual():
    user_choice = input("📌 Account (y) or Page (n)? (y/N/d): ")
    user = input("👤 USER ID/EMAIL: ")
    passw = input("🔑 PASSWORD: ")
    linex()
    cuser(user, passw, user_choice)

# Manual from File
def ManFile():
    file_path = input("📂 Enter file path: ")
    if os.path.isfile(file_path):
        try:
            user_choice = input("📌 Account (y) or Page (n)? (y/N/d): ")
            with open(file_path, 'r') as file:
                for line in file:
                    user_pass = line.strip().split('|')
                    process_users([user_pass], user_choice)
        except Exception as e:
            console.print(Panel(f"❌ Error reading the file: {e}", style="red"))
    else:
        console.print(Panel("❌ File not found!", style="red"))

# Auto from File
def Auto():
    directory = '/sdcard'
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    if not txt_files:
        console.print(Panel("❌ No .txt files found!", style="red"))
        return
    
    for i, filename in enumerate(txt_files, start=1):
        console.print(f"    {i}. {filename}")
    
    try:
        linex()
        choice = int(input("➡️ Choose: "))
        if 1 <= choice <= len(txt_files):
            selected_file = os.path.join(directory, txt_files[choice - 1])
            if os.path.isfile(selected_file):
                try:
                    user_choice = input("📌 Account (y) or Page (n)? (y/N/d): ")
                    with open(selected_file, 'r') as file:
                        for line in file:
                            user_pass = line.strip().split('|')
                            process_users([user_pass], user_choice)
                except Exception as e:
                    console.print(Panel(f"❌ Error reading the file: {e}", style="red"))
            else:
                console.print(Panel("❌ File not found!", style="red"))
        else:
            console.print(Panel("❌ Invalid option!", style="red"))
    except ValueError:
        console.print(Panel("❌ Invalid input!", style="red"))

# Process Users
def process_users(user_list, user_choice):
    for user_pass in user_list:
        if len(user_pass) == 2:
            user, passw = user_pass
            cuser(user, passw, user_choice)
        else:
            console.print(Panel(f"❌ Invalid format in line: {user_pass}", style="red"))

# Generate User-Agent
def kyzer():
    android_version = f"{random.randint(5, 14)}.{random.randint(0, 9)}"
    fb_version = f"{random.randint(100, 999)}.0.0.{random.randint(10, 99)}.{random.randint(100, 999)}"
    fbbv = random.randint(100000000, 999999999)
    
    manufacturers = ["Samsung", "Realme", "Oppo", "Vivo", "Xiaomi"]
    manufacturer = random.choice(manufacturers)
    
    models = [
        f"SM-{random.randint(100, 9999)}U", f"RMX{random.randint(1000, 9999)}", f"CPH{random.randint(1000, 9999)}",
        f"V{random.randint(1000, 9999)}", f"M{random.randint(1000, 9999)}"
    ]
    
    model = random.choice(models)

    ua = f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/{manufacturer}) [FBAN/FB4A;FBAV/{fb_version};FBBV/{fbbv}]"
    
    return ua

# Login System
def cuser(user, passw, user_choice):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()),
        'email': user, 'password': passw, 'access_token': accessToken, 'method': 'auth.login'
    }
    
    headers = {'User-Agent': kyzer(), 'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post("https://b-graph.facebook.com/auth/login", headers=headers, data=data).json()
    
    if "session_key" in response:
        console.print(Panel(f"✅ Success: {user} extracted!", style="green"))
        with open('/sdcard/Test/toka.txt', 'a') as f:
            f.write(f'{response["access_token"]}\n')
    else:
        console.print(Panel(f"❌ Failed: {user} isn't extracted.", style="red"))

# Start
Initialize()
