def main():
    greeting = input("Greeting:")
    amount = value(greeting)
    print(f"${amount}")
def value(greeting):
    whisper = greeting.lower()
    if whisper.startswith("hello"):
        return "0"
    elif whisper.startswith("h"):
        return "20"
    else:
        return "100"
    return value
if __name__ == "__main__":
    main()