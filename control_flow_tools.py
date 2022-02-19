# match statements with variables.

var = (8,0)
match var:
    case (0,y):
      print ("on the y axis")
    case (x,0):
        print ("on the x axis")
    case (0,0):
        print ("the point of origin")
    case (x,y):
        print ("not on the axis")    
        