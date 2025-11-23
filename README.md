RECIPE AND INGREDIENTS MANAGER 

OVERVIEW

The Web App (Recipe & Ingredient Manager): This is your all-in-one visual dashboard, contained entirely within the index.html file. It uses Tailwind CSS for its modern look, and JavaScript handles all the interactive features—from tracking your inventory and planning weekly meals to generating shopping lists. Crucially, it uses Firebase Firestore to save and retrieve all your data in real-time, making it a persistent, dynamic application that runs in your browser.

The Python Tool (Command-Line Manager): This is a separate, text-based application designed for data management via the terminal. The core logic is split between two files: main.py, which is the application's entry point and handles the user menu, and db_manager.py, which contains the RecipeDBManager class, responsible only for storing and accessing the underlying data. Finally, the requirements.txt file lists necessary libraries like tabulate for clean console output.


FEATURES

1. The Web App: Your Super-Smart Kitchen Assistant
  This app gives you total control over your cooking life, all from a clean interface in your browser:
    Recipe Box Organizer: You can easily jot down, save, and toss out your recipes. No more messy notes—it keeps track of your dish details (like cuisine       and how many people it feeds).
    Fridge Stock Tracker: You always know exactly what's in your fridge and pantry. When you buy something, you add it; when you use it, you subtract it.       The app even gives you a little warning if a staple ingredient is running low!
    Effortless Meal Planning: You can drag-and-drop your favorite recipes onto a calendar for the entire week. Need to change Friday's dinner? It's one         click to swap or clear the plan.
    Instant Shopping List: This is the best part! It looks at all the meals you planned, checks your current fridge stock, and instantly tells you: "Here       is exactly what you need to buy and nothing more." It even tells you if you can actually cook a recipe based on what you have right now.

2. The Python Tool: Your Data Backup & Control Center
  This tool is more for power users who like to manage data directly via commands:
    Direct Access: It lets you bypass the visual interface and work directly with your recipes and ingredient lists using simple text commands in your          computer's terminal.
    Clean Readouts: Instead of dumping raw data, it uses a special tool (tabulate) to neatly organize and present your information in clean, easy-to-read       tables.
Essentially, the Web App is for daily use and planning, and the Python Tool is for efficient, text-based data management!

TECHNOLOGIES

Essential Tools & Technologies
   Database: Firestore for real-time, collaborative inventory management.
   Front-End: Mobile-first design using React/Angular and Tailwind CSS.
   Data Entry: Computer Vision/Barcode Scanning for fast inventory logging.
   Automation: Cloud Functions for automated expiry alerts (Nudge Theory).

STEPS TO INSTALL AND RUN THE PROJECT

1. Python Tool (Command-Line Manager)
This project is run through your terminal (Command Prompt, PowerShell, or VS Code's terminal).
  A. Installation (One-Time Setup)
    Check Python: Ensure you have Python installed (version 3.x is recommended). You can check by typing:
    Install Dependencies: The Python tool relies on external libraries (like tabulate). You must install them using the requirements.txt file. Navigate to      the folder containing your Python files and run this commands .
  B. How to Run
    Execute the Main Script: Stay in the folder containing your Python files and run the main application file:
    Interaction: The application will start and present the main menu, allowing you to interact with your data manager via text commands.
2. Web Application (Recipe and Ingredient Manager)
This project runs in your browser and requires a special local server due to its use of Firebase.
  A. Installation (VS Code Setup)
    Install Extension: If you haven't already, install the Live Server extension by Ritwick Dey in Visual Studio Code.
    This tool acts as a simple web server, which is necessary because local files often cannot communicate with external services like Firebase.
  B. How to Run
    Open the File: Open the index.html file in VS Code.
    Launch Live Server: Right-click anywhere in the index.html file and select "Open with Live Server" (or click the "Go Live" button in the bottom-right       status bar).
    View the App: Your default web browser will open (usually at an address like http://127.0.0.1:5500/index.html).
    Local Warning: You will see the message: "Running locally: Using dummy config. Data is NOT persistent or shared." This is expected when using Live          Server, confirming the app is running correctly for testing.
Note: The web application is fully functional and uses a local dummy configuration for testing outside of the Canvas environment.

INSTRUCTIONS

The testing process begins by validating the Web App (The Browser Dashboard) by first adding a test recipe and planning it for a specific day, ensuring it appears correctly in both the Recipes and Plan sections. Next, navigate to the Inventory section to test stock tracking by both adding and subtracting a quantity of a test ingredient (like "Flour") to verify that the quantity updates accurately. The critical validation occurs on the Reports tab: check the Shopping List to confirm the test ingredient's status is "✅ Stocked" based on the previous inventory updates, and observe the Recipe Readiness section to confirm the test recipe is correctly flagged as "Missing Ingredients" (due to missing placeholder ingredients). The Web App testing concludes by deleting the test recipe to confirm that the related plan and report data are instantly cleared. Following this, validate the Python Tool (The Terminal Workhorse) by running python main.py in the terminal; the application must load the main menu with options displayed in neatly organized tables, confirming the tabulate library is working. Finally, use the menu options to successfully add a new recipe and then list all recipes, verifying that the new entry appears in a formatted table before exiting the program gracefully.



