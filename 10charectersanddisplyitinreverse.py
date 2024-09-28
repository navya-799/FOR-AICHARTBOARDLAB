def read_and_reverse(file_name, n):
    try:
        with open(file_name, 'r') as file:
            content = file.read(n)
            reversed_content = content[::-1]  
            print(reversed_content)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
file_name = 'example.txt'
n = 10
read_and_reverse(file_name, n)
