# Read from source file and write uppercase content to destination file

source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    with open(source_file, 'r') as f1:
        content = f1.read()

    # Convert to uppercase
    upper_content = content.upper()

    with open(destination_file, 'w') as f2:
        f2.write(upper_content)

    print("\nFile copied successfully in UPPERCASE!")

    # Display contents
    print("\n--- Source File Content ---")
    print(content)

    print("\n--- Destination File Content ---")
    print(upper_content)

except FileNotFoundError:
    print("File not found! Please check the file name.")
