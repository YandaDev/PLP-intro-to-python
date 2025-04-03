# This program helps you work with files and handle errors

# Read a file, modify it, and save to a new file
def file_challenge():
    print("\n--- File Read & Write Challenge ---")
    print("We'll read a file, change its text to uppercase, and save it to a new file.")
    
    try:
        # Ask for file names
        original_file = input("Enter the name of the file to read (e.g., story.txt): ")
        new_file = input("Enter a name for the new file (e.g., new_story.txt): ")
        
        # Open and read the original file
        with open(original_file, 'r') as file:
            original_text = file.read()
        
        # Modify the text (make it uppercase)
        modified_text = original_text.upper()
        
        # Save to the new file
        with open(new_file, 'w') as file:
            file.write(modified_text)
        
        print(f"Success! Your modified file is saved as '{new_file}'")
    
    except FileNotFoundError:
        print(f"Oops! Couldn't find '{original_file}'. Please check the file name.")
    except:
        print("Something went wrong. Please try again.")

# Practice opening files with error handling
def error_lab():
    print("\n--- Error Handling Lab ---")
    print("Try opening files. We'll help if there are problems.")
    
    while True:
        file_name = input("\nEnter a file name to open (or type 'quit' to exit): ")
        
        if file_name.lower() == 'quit':
            print("Goodbye!")
            break
        
        try:
            # Try to open and read the file
            with open(file_name, 'r') as file:
                print("\nFile contents:")
                print(file.read())
            break  # Exit if successful
            
        except FileNotFoundError:
            print(f"Sorry, '{file_name}' doesn't exist. Try another file.")
        except PermissionError:
            print(f"You don't have permission to open '{file_name}'.")
        except:
            print("Couldn't read the file. It might be damaged or not a text file.")

# Main program
print("=== Python File Handling Practice ===")
print("Let's learn to work with files safely!\n")

file_challenge()  # Do the first part
error_lab()      # Then do the second part

print("\nGreat job! You've practiced file handling and error handling.")