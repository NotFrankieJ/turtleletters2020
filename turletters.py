import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.left(90)
        tur.forward(15)
        tur.left(90)
        tur.fd(20)
        #fix
        tur.pu()
        tur.left(180)
        tur.fd(35)
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
tur.right(-90)
tur.forward(60)
tur.right(180)
tur.forward(60)
tur.left(90)
tur.forward(40)
	    pass

    elif letter == "M":
tur.left(45)
tur.forward(20)
tur.right(90)
tur.forward(20)
tur.left(90)
tur.forward(20)
tur.right(90)
tur.forward(20)
	    pass
    elif letter == "N":
tur.left(90)
tur.forward(40)
tur.right(135)
tur.forward(40)
tur.left(135)
tur.forward(40)

	    pass
    elif letter == "O":
tur.left(90)
tur.forward(60)
tur.left(90)
tur.forward(40)
tur.left(90)
tur.forward(60)
tur.left(90)
tur.forward(40)
	    pass
    elif letter == "P":
      tur.left(90)
      tur.forward(60)
tur.right(90)
tur.forward(40)
tur.right(90)
tur.forward(40)
tur.right(90)
tur.forward(40)
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
