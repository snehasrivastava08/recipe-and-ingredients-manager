# main.py
from db_manager import RecipeDBManager
from utils import hash_password, get_valid_input, clear_screen, display_table
import sys

# --- 1. AUTHENTICATION ---

def authenticate_user(db_manager):
    """Handles simple login/registration (User Management)."""
    print("\n--- 👤 Login / Register ---")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    hashed_pword = hash_password(password)
    
    user = db_manager.fetchone("SELECT id FROM users WHERE username = ? AND password_hash = ?", (username, hashed_pword))

    if user:
        print(f"\n✅ Welcome back, {username}!")
        return True
    else:
        # Check if user exists, if not, prompt to register
        existing_user = db_manager.fetchone("SELECT id FROM users WHERE username = ?", (username,))
        if not existing_user:
            print("\nUser not found. Would you like to register this new account? (y/n)")
            if input().lower() == 'y':
                if db_manager.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_pword)):
                    print(f"✅ User {username} registered and logged in!")
                    return True
        
        print("❌ Invalid username or password.")
        return False


# --- 2. APPLICATION CLASS ---

class RecipeManagerApp:
    """Encapsulates all functional modules and main loop."""
    
    def __init__(self):
        self.db = RecipeDBManager()
        self.running = True
        
    def main_menu(self):
        """Displays the main menu (Logical Workflow)."""
        clear_screen()
        print("="*40)
        print("  🧑‍🍳 Recipe & Ingredient Manager")
        print("="*40)
        print("1. 📚 Manage Recipe Book")
        print("2. 🥕 Manage Ingredient Inventory")
        print("3. 📋 Manage Meal Planner")
        print("4. 📊 Run Reports / Simulation")
        print("0. 🚪 Exit")
        print("="*40)
        
        choice = get_valid_input("Enter your choice: ", int)
        
        if choice == 1: self._recipe_menu()
        elif choice == 2: self._inventory_menu()
        elif choice == 3: self._meal_planner_menu()
        elif choice == 4: self._report_menu()
        elif choice == 0: self.running = False
        else:
            print("❌ Invalid option.")
            input("Press Enter to continue...")

    # --- MODULE 1: RECIPE BOOK (CRUD) ---
    # (Implementation details omitted for brevity, but they contain all CRUD logic 
    # as described in the E2E analysis, using self.db methods and utils.py functions)
    # ... placeholder for full implementation ...
    
    def _recipe_menu(self):
        """Placeholder for Recipe CRUD menu."""
        while True:
            clear_screen()
            print("\n--- 📚 Recipe Book Management ---")
            print("1. Add Recipe (Create) | 2. View All (Read)")
            print("3. Edit Recipe (Update) | 4. Delete Recipe (Delete)")
            print("0. Back to Main Menu")
            
            choice = get_valid_input("Enter your choice: ", int)
            
            if choice == 1: self._add_recipe()
            elif choice == 2: self._view_recipes()
            # ... other CRUD functions ...
            elif choice == 0: return
            else: print("❌ Invalid option.")
            input("\nPress Enter to continue...")
            
    def _add_recipe(self):
        print("\n--- Adding New Recipe ---")
        title = get_valid_input("Recipe Title: ")
        # ... logic for inserting recipe and ingredients ...
        if self.db.execute("INSERT INTO recipes (title, cuisine, servings) VALUES (?, ?, ?)", (title, 'placeholder', 1)):
            print(f"✅ Recipe '{title}' added (full ingredient logic omitted here, but present in final project).")

    def _view_recipes(self):
        recipes = self.db.fetchall("SELECT id, title, cuisine, servings FROM recipes")
        display_table(recipes, ["ID", "Title", "Cuisine", "Servings"], "All Recipes")
        
    # --- MODULE 2: INVENTORY MANAGEMENT (CRUD) ---
    def _inventory_menu(self):
        """Placeholder for Inventory CRUD menu."""
        clear_screen()
        print("Inventory Management is active. (CRUD logic omitted for brevity)")
        input("Press Enter to continue...")
        
    # --- MODULE 3: MEAL PLANNER (CRUD) ---
    def _meal_planner_menu(self):
        """Placeholder for Meal Planner CRUD menu."""
        clear_screen()
        print("Meal Planner is active. (CRUD logic omitted for brevity)")
        input("Press Enter to continue...")

    # --- REPORTS & SIMULATION (Analytics & Simulation) ---
    def _report_menu(self):
        """Placeholder for Reports/Simulation menu."""
        clear_screen()
        print("Reports & Simulation are active. (Shopping List and Stock Check logic omitted for brevity)")
        input("Press Enter to continue...")

# --- 3. MAIN EXECUTION ---
if __name__ == "__main__":
    
    # 1. Install check
    try:
        from tabulate import tabulate # Check for required library
    except ImportError:
        print("🔴 Required library 'tabulate' not found.")
        print("Please run: pip install -r requirements.txt")
        sys.exit(1)
        
    app = RecipeManagerApp()
    
    # 2. Authentication flow
    print("Welcome to the Recipe Manager.")
    while not authenticate_user(app.db):
        print("Please try logging in again.")
        
    # 3. Main Application Loop
    while app.running:
        app.main_menu()

    # 4. Cleanup
    app.db.close()
    print("\nGoodbye! Data saved to recipe_data.db.")