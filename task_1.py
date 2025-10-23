import math

def total_salary(path):
    """
    Calculates the total and average salary from a file.

    The file should contain one record per line, with each line formatted as:
    <name>,<salary>
    Example:
        John,5000
        Jane,6000

    Args:
        path (str): The path to the salary file.

    Returns:
        tuple: A tuple containing:
            - total_salary (float): The sum of all salaries in the file.
            - average_salary (float): The average salary, or 0 if the file is not found or empty.

    Prints:
        "File not found" if the specified file does not exist.
        "File cannot be read (corrupted or invalid encoding)" if the file is damaged.
    """
    salary_total = 0
    average_salary = 0

    try:
        with open(path, encoding="utf-8") as file:
            file_lines = file.readlines()
    except FileNotFoundError:
        print("File not found")
        return salary_total, average_salary
    except UnicodeDecodeError:
        print("File cannot be read (corrupted or invalid encoding)")
        return salary_total, average_salary
    except OSError as e:
        print(f"OS error occurred: {e}")
        return salary_total, average_salary

    for line in file_lines:
        [_, salary] = line.strip().split(',')
        print(salary)
        salary = int(salary)
        salary_total = salary + salary_total

    average_salary = math.ceil(salary_total / len(file_lines))

    return salary_total, average_salary

# Example usage
total, average = total_salary("./files/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
