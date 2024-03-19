# sample_python_code.py

def greet(name):
    """This function greets the user."""
    return f"Hello, {name}!"

def main():
    """Main function."""
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()
