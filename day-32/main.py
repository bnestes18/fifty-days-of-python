import re

def password_validator():
    errors = []
    
    password = ""
    while not password:
        print("""Your password must meet the following requirements: 
              at least one uppercase letter, one lowercase letter, one digit and 8 characters long.""")
        password = input("Password: ")
        
        lowercase = re.compile(r"[a-z]")
        hasLower = re.search(lowercase, password)
        
        uppercase = re.compile(r"[A-Z]")
        hasUpper = re.search(uppercase, password)
        
        digits = re.compile(r"\d")
        hasDigit = re.search(digits, password)
        
        if len(password) < 8:
            errors.append("Password needs to be longer than 8 characters.")
        if not hasLower:
            errors.append("Password does not have at least one lowercase letter.")
        if not hasUpper:
            errors.append("Password does not have at least one uppercase letter.")
        if not hasDigit:
            errors.append("Password does not have at least one digit.")
            
        if len(errors) > 0:
            print("Cannot accept password due to the following errors:\n")
            for e in errors:
                print(e)
            password = ""
        else:
            return password
            
print("password_validator function: ", password_validator())

# Extra Challenge!!!
def email_validator(emails):
    valid_emails = []
    
    for email in emails:
        if '@' in email and email.count('@') == 1 and email[-4:] == '.com':
            if not email[0] == '@':
                valid_emails.append(email)
                
    if len(valid_emails) == 0:
        return "all emails are invalid."
    return valid_emails

print("email_validator function:", email_validator(['@ben@mail.com', '@john@mail.cm', '@kenny@gmail.com']))