import re
import sys

def main():
    print(convert(input("Hours: ")))
    
def convert(s):
    if matches := re.search(r"([1-9]|1[0-2]) :?( [0-5][0-9] )?(AM|PM) to ([1-9]|1[0-2]) :?( [0-5][0-9] )?(AM|PM)", s):
        matches = matches.groups("0")
        hour1 = int(matches[0])
        hour2 = int(matches[3])
        if matches[2] == "PM":
              if 0 < hour1 < 12:
                  hour1 += 12
        elif hour1 == 12 and matches[2] =="AM":
            hour1 = 0
        if matches[5] == "PM":
              if 0 < hour2 < 12:
                  hour2 += 12
        elif hour2 == 12 and matches[5] =="AM":
            hour2 = 0
        return f"{hour1:02} : {int(matches[1]):02} to {hour2:02} : {int(matches[4]):02}"
    else:
          raise ValueError("Invalid Format")
      
      
      
if __name__ == "__main__":
    main()   