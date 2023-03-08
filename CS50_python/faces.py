def main():
    emoji = input()
    face = convert(emoji)
    print(face)
    
def convert(this):
    return(this.replace(":)", "🙂").replace(":(", "🙁"))
    
main()