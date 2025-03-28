def read_file(file_path):
    """Зчитує всі рядки з файлу та повертає їх у вигляді списку."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

