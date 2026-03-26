import os

# Define the target directory and filename
# Using os.path.join for cross-platform compatibility (Windows/Mac/Linux)
target_dir = os.path.join("extra_exercises", "JSON_Experiments")
file_path = os.path.join(target_dir, "Guestbook.txt")

# Ensure the directories exist before attempting to write
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"Created directory: {target_dir}")

print("--- Welcome to the Guestbook! ---")

# 1. Ask for the user's name
name = input("What is your name? ")

# 2. Save the name to the file in the specific folder
try:
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(name + "\n")
    print(f"\nThank you {name}! Your name has been saved to: {file_path}\n")
except Exception as e:
    print(f"An error occurred while saving: {e}")

# 3. Read and display the current list of guests
print("List of previous guests:")
if os.path.exists(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            if content.strip():
                print(content)
            else:
                print("(The guestbook is currently empty)")
    except Exception as e:
        print(f"Error reading the file: {e}")
else:
    print("No guestbook file found yet. You are the first guest!")

print("--------------------------------")