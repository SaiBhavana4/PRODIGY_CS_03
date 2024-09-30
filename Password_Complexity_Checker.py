import string

def evaluate_password(password):
    """
    Assesses the strength of a password based on various factors such as length and character types.

    Args:
        password: The password to evaluate.

    Returns:
        A tuple of (password strength, suggestions for improvement).
    """
    criteria_met = 0
    suggestions = []
    
    # Check the password length
    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    else:
        criteria_met += 1

    # Check if there are both uppercase and lowercase letters
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        criteria_met += 1
    else:
        suggestions.append("Use a mix of both uppercase and lowercase letters.")

    # Check if it contains any digits
    if any(char.isdigit() for char in password):
        criteria_met += 1
    else:
        suggestions.append("Include at least one number.")

    # Check for special characters
    if any(char in string.punctuation for char in password):
        criteria_met += 1
    else:
        suggestions.append("Include at least one special character (e.g., !@#$).")

    # Determine the password strength based on criteria met
    if criteria_met == 4:
        if len(password) >= 12:
            strength = "Very Strong"
        else:
            strength = "Strong"
    elif criteria_met == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions

def get_password_input():
    """
    Gets a password from the user and provides feedback on its strength.
    """
    password = input("Enter a password to evaluate: ")
    
    # Assess the password strength
    strength, suggestions = evaluate_password(password)
    
    # Display the results
    print(f"Password Strength: {strength}")
    
    if suggestions:
        print("\nSuggestions for improvement:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Your password is very strong!")

# Main function to run the password checker
if __name__ == "__main__":
    get_password_input()
