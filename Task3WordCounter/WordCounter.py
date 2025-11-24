#Task 3: Word Counter
#  Read the content of a file.
#  Split the content into words and count them.
#  Handle exceptions, such as file not found

def word_counter(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when trying to open '{file_path}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
if __name__ == "__main__":
    file_path = input("Enter the path to the file you want to count words in: ")
    word_counter(file_path)