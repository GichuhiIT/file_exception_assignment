# file_read_write.py

# Read from an existing file
with open("input.txt", "r", encoding="utf-8") as infile:
    content = infile.read()

# Modify the content (e.g., make it uppercase)
modified_content = content.upper()

# Write the modified content into a new file
with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.write(modified_content)

print("File has been read, modified, and written successfully ✅")
