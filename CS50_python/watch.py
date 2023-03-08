import re
import sys

def main():
    print(parse(input("HTML: ")))
    
    
def parse(iframe):
    if matches := re.search(r'src="(https?://)(?:www\.)?(youtu)(be)\.com/embed(/.*?)"', iframe):
        link = matches.groups()
        return f"{link[0]}{link[1]}.{link[2]}{link[3]}"
    else:
        return None
    
if __name__ =="__main__":
    main()    