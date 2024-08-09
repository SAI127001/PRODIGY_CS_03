from pyfiglet import figlet_format
import re

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def check_password_complexity(password):
    # Define criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess the strength of the password based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        return color.GREEN + "Strong password!!!!!!!!!!"
    else:
        feedback = color.RED + "Weak password. Consider the following improvements:\n"
        if not length_criteria:
            feedback += "- Ensure the password is at least 8 characters long\n"
        if not uppercase_criteria:
            feedback += "- Include at least one uppercase letter\n"
        if not lowercase_criteria:
            feedback += "- Include at least one lowercase letter\n"
        if not digit_criteria:
            feedback += "- Include at least one digit\n"
        if not special_char_criteria:
            feedback += "- Include at least one special character (!@#$%^&*(),.?\":{}|<>)\n"

        return feedback

def main():
    print(color.BOLD + color.CYAN + figlet_format("PASSWORD COMPLEXITY CHECKER", font="slant")+ color.END)

    # Get user input for the password
    password = input("Enter your password: ")
    print("")

    # Check and provide feedback on the password complexity
    result = check_password_complexity(password)
    print(result)

if __name__ == "__main__":
    main()
