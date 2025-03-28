import pytest
from main import write_to_file, compare_files, read_file


@pytest.fixture
def file_setup(tmpdir):
    return tmpdir


# Test for the write_to_file function
def test_write_to_file(file_setup):
    same_lines = ["Apple", "Orange"]
    diff_lines = ["Banana", "Grapes"]

    # Записуємо в same.txt та diff.txt
    write_to_file(file_setup.join("same_test.txt"), same_lines)
    write_to_file(file_setup.join("diff_test.txt"), diff_lines)

    # Перевіряємо, чи створюються файли правильно
    with open(file_setup.join("same_test.txt"), 'r') as f:
        content = f.read()
        assert "Apple" in content
        assert "Orange" in content

    with open(file_setup.join("diff_test.txt"), 'r') as f:
        content = f.read()
        assert "Banana" in content
        assert "Grapes" in content


# Test for the compare_files function
@pytest.fixture
def file_setup_compare(tmpdir):
    # Створюємо тимчасові файли для тестування
    file1 = tmpdir.join("file1.txt")
    file2 = tmpdir.join("file2.txt")
    file1.write("Apple\nOrange\nBanana\n")
    file2.write("Apple\nOrange\nGrapes\n")
    return str(file1), str(file2)


@pytest.mark.parametrize(
    "file1_content, file2_content, expected_same, expected_diff",
    [
        ("Apple\nOrange\nBanana\n", "Apple\nOrange\nGrapes\n",
         ["Apple", "Orange"], ["Banana", "Grapes"]),

        ("Red\nBlue\nGreen\n", "Blue\nGreen\nYellow\n",
         ["Blue", "Green"], ["Red", "Yellow"]),

        ("Cat\nDog\nElephant\n", "Cat\nDog\nElephant\n",
         ["Cat", "Dog", "Elephant"], []),
    ]
)
def test_compare_files(file_setup_compare, file1_content, file2_content, expected_same, expected_diff):
    file1, file2 = file_setup_compare
    # Записуємо вміст у файли
    with open(file1, 'w') as f1, open(file2, 'w') as f2:
        f1.write(file1_content)
        f2.write(file2_content)

    same_lines, diff_lines = compare_files(file1, file2)

    assert same_lines == expected_same
    assert diff_lines == expected_diff


# Test for the read_file function
@pytest.fixture
def file_setup_read(tmpdir):
    file1 = tmpdir.join("file1.txt")
    file1.write("Apple\nOrange\nBanana\n")
    return str(file1)

def test_read_file(file_setup_read):
    file1 = file_setup_read
    lines = read_file(file1)
    assert "Apple" in lines
    assert "Orange" in lines
    assert "Banana" in lines
    assert len(lines) == 3
