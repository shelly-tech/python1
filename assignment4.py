def modify_file_content(content):
    """
    Modify the content of the file.
    This example converts all text to uppercase.
    You can customize this function to apply other transformations.
    """
    return content.upper()

def main():
    # Ask the user for the input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            original_content = infile.read()

        # Modify the content
        modified_content = modify_file_content(original_content)

        # Create a new filename for the modified content
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")

if __name__ == "__main__":
    main()
