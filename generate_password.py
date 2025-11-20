'''python
import random
import string

def generate_password(length=12, use_symbols=True, use_numbers=True ):
    """
    Generate a random password
    Args:
        length (int) : password length
        use_symbols (bool) : Include special symbols
        use_numbers (bool) : Include numbers
    Returns:
        str : Generated password
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    if use_symbols :
        characters += string.punctuation
    if use_numbers :
        characters += string.digits
    if not characters :
        return "Error : You must select at least one character type "
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Random Password Generator")
    print("=" * 30 )

    try :
        length = int(input("Enter password length (default 12):") or 12 )
        use_symbols = input("Include special symbols ? (Y/N , default y):").lower() != 'n'
        use_numbers = input("Include numbers ? (Y/N , default y):").lower() != 'n'

        password = generate_password(length  , use_symbols , use_numbers)

        print(f"\n Generated_password: {password}")
        print(f"Length: {len(password)} characters")

    except ValueError :
        print("Error: please enter a valid number for length")

if __name__ = "__main__":
    main()














    

