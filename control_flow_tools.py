#match statements
number =int(input("code"))
def country_name(code):
    match code:
      case 254:
        return ("Kenya")                                                                   
      case 256:
          return ("Uganda")
      case 247:
          return ("tanzania")
      case _:
          return ("Notfound")
print (country_name(number) )
