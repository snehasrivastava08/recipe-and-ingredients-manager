# db_manager.py
import sqlite3

class RecipeDBManager :
    """Handles all database connection and raw SQLite CRUD operations."""
    def __init__(self, db_name="recipe_data.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self._initialize_db()

    def _initialize_db(self):
        """Connects and creates tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            
            # --- Functional Modules/Entities ---
            
            # User Management Table (Security)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """)
            
            # Recipe Book Table (Module 1)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    cuisine TEXT,
                    servings INTEGER
                )
            """)
            
            # Ingredient Inventory Table (Module 2)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory (
                    name TEXT PRIMARY KEY,
                    quantity REAL NOT NULL,
                    unit TEXT
                )
            """)
            
            # Recipe Ingredients (Relationship Table - Reliability/Integrity)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS recipe_ingredients (
                    recipe_id INTEGER,
                    ingredient_name TEXT,
                    quantity REAL NOT NULL,
                    unit TEXT,
                    FOREIGN KEY(recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
                    FOREIGN KEY(ingredient_name) REFERENCES inventory(name) ON DELETE NO ACTION,
                    PRIMARY KEY (recipe_id, ingredient_name)
                )
            """)
            
            # Meal Plan Table (Module 3)
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS meal_plan (
                    day TEXT PRIMARY KEY,
                    recipe_id INTEGER,
                    FOREIGN KEY(recipe_id) REFERENCES recipes(id)
                )
            """)

            self.conn.commit()

        except sqlite3.Error as e:
            print(f"🔴 Database Critical Error: {e}")
            if self.conn:
                self.conn.close()
            exit() 

    def close(self):
        if self.conn:
            self.conn.close()
            
    def execute(self, query, params=()):
        """Wrapper for executing queries with error handling."""
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"\n🔴 Database Error: {e}")
            return False

    def fetchall(self, query, params=()):
        """Wrapper for fetching all results."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=()):
        """Wrapper for fetching one result."""
        self.cursor.execute(query, params)
        return self.cursor.fetchone()