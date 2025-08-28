# error_handling_lab.py

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print("File content:\n")
        print(file.read())
except FileNotFoundError:
    print(f"❌ Error: The file '{filename}' does not exist.")
except PermissionError:
    print(f"❌ Error: You don’t have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ An unexpected error occurred: {e}")
