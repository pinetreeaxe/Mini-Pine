from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

def test_get_files_info():
    print('Testing get_files_info:')
    
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print()

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print()

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print()

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print()

def test_get_file_content():
    print('Testing get_file_content:')
    
    #result = get_file_content("calculator", "lorem.txt")
    #print('Result reading "lorem.txt" (should truncate if larger than 10000 chars):')
    #print(result)
    #print()

    result = get_file_content("calculator", "main.py")
    print('Result reading "main.py":')
    print(result)
    print()

    result = get_file_content("calculator", "pkg/calculator.py")
    print('Result reading "pkg/calculator.py":')
    print(result)
    print()

    result = get_file_content("calculator", "/bin/cat")
    print('Result reading "/bin/cat" (should produce error):')
    print(result)
    print()

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print('Result reading non-existent "pkg/does_not_exist.py" (should produce error):')
    print(result)
    print()

def test_write_file():
    print('Testing write_file:')

    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

def test_run_python_file():
    print('Testing run_python_file:')

    result = run_python_file("calculator", "main.py")

    result = run_python_file("calculator", "main.py", ["3 + 5"]) 
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print(result)


if __name__ == "__main__":
    #test_get_files_info()
    #test_get_file_content()
    #test_write_file()
    test_run_python_file()