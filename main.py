def read_file(file_path):
    """Зчитує всі рядки з файлу та повертає їх у вигляді списку."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

def compare_files(file1, file2):
    """
    Порівнює два файли та повертає:
    - спільні рядки (same)
    - відмінні рядки (diff)
    """
    lines1 = read_file(file1)
    lines2 = read_file(file2)

    same_lines = [line for line in lines1 if line in lines2]
    diff_lines = [line for line in lines1 + lines2 if line not in same_lines]

    return same_lines, diff_lines
