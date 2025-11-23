# utils.py
import hashlib
from tabulate import tabulate
import os
import sys

def hash_password(password):
    """Hashes a password using SHA-256 for storage (Security)."""
    return hashlib.sha256(password.encode()).hexdigest()

def get_valid_input(prompt, data_type=str, error_msg="Invalid input. Please try again."):
    """Validates user input type (Error Handling)."""
    while True:
        try:
            value = input(prompt).strip()
            if value.lower() == 'back':
                return 'back' # Special return for menu navigation
            
            if data_type == str:
                return value
            elif data_type == int:
                return int(value)
            elif data_type == float:
                return float(value)
            else:
                return data_type(value)
        except ValueError:
            print(f"🔴 {error_msg}")

def clear_screen():
    """Clears the console for a cleaner menu (Usability)."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_table(data, headers, title=""):
    """Displays data in a formatted table (Usability)."""
    if title:
        print(f"\n--- {title} ---")
    if not data:
        print("ℹ️ No records found.")
        return
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))