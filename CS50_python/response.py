import validators

def main():
    print(validate(input("Email: ")))
    
def validate(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"
        
if __name__ == "__main__":
    main()