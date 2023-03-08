def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ZeroDivisionError, ValueError, TypeError) as error:
            pass           
    print(gauge(percentage))
     
    
def convert(fraction):
      x, y = fraction.split("/")
      division = int(x) / int(y)
      if 0 <= division <= 1:
          return division
      
          
def gauge(division):
      percentage = 100 * division
      if percentage <= 1:
          return "E"
      elif percentage >= 99:
          return "F"
      else:
          return f"{int(percentage)}%"
          
if __name__ == "__main__":
    main()