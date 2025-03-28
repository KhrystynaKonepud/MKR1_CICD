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

def write_to_file(filename, lines):
    """Записує рядки у файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("\n".join(lines) + "\n" if lines else "")


def main():
    file1 = input("Введіть назву першого файлу: ")
    file2 = input("Введіть назву другого файлу: ")

    same, diff = compare_files(file1, file2)

    write_to_file("same.txt", same)
    write_to_file("diff.txt", diff)

    print("Файли same.txt і diff.txt успішно створено!")


if __name__ == "main":
    main()
