#  Write a Python program to read an entire text file.

def read_file():
    file_name = input("Enter the file name: ").strip()

    try:
        # Safely opens the file and ensures it closes automatically
        with open(file_name, 'r') as file:
            # Read the entire content
            content = file.read()
            # Print the content
            print("\n✅ File Content:\n")
            print(content)

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the file name and path.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

read_file()




# # Ask the user for the file name
# file_name = input("Enter the file name: ")
# file = open(file_name, 'r')
# content = file.read()
# print("File Content:\n")
# print(content)
# # Close the file
# file.close()