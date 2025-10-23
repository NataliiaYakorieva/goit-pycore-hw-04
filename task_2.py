def get_cats_info(path):
    """
    Reads cat information from a file and returns a list of dictionaries with cat data.

    The file should contain one record per line, with each line formatted as:
    <id>,<name>,<age>
    Example:
        60b90c1c13067a15887e1ae1,Tayson,3
        60b90c2413067a15887e1ae2,Vika,1

    Args:
        path (str): The path to the cats info file.

    Returns:
        list: A list of dictionaries, each containing:
            - 'id' (str): The cat's ID.
            - 'name' (str): The cat's name.
            - 'age' (str): The cat's age.

    Prints:
        "File not found" if the specified file does not exist.
        "File cannot be read (corrupted or invalid encoding)" if the file is damaged.
        "OS error occurred: <error message>" for other OS-related errors.
    """
    result = []

    try:
        with open(path, encoding="utf-8") as file:
            file_lines = file.readlines()
    except FileNotFoundError:
        print("File not found")
        return result
    except UnicodeDecodeError:
        print("File cannot be read (corrupted or invalid encoding)")
        return result
    except OSError as e:
        print(f"OS error occurred: {e}")
        return result

    for line in file_lines:
        [cat_id, name, age] = line.strip().split(',')
        result.append({"id": cat_id, "name": name, "age": age})

    return result

# Example usage
cats_info = get_cats_info("./files/cats_file.txt")
print(cats_info)