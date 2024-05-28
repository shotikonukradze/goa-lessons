from turtle import*


#square
width(7)
color("orange")
begin_fill()   
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#door
width(7)

forward(80)
left(90)

color("purple")
begin_fill()
forward(90)
right(90)

forward(45)
right(90)
forward(90)
end_fill()


penup()
goto(200,200)
pendown()

#roof

color("red")
begin_fill()
right(150)
forward(200)

left(120)
forward(200)
end_fill()

#next roof(left)


color("red")
begin_fill()
right(110)
forward(150)
left(95)
forward(150)
left(135)
forward(200)
end_fill()

color("orange")
begin_fill()
penup()
goto(-202,202)
pendown()
right(90)
forward(202)
left(90)
forward(203)
end_fill()

width(10)
color("red")
penup()
goto(-203,203)
pendown()
forward(200)


#door N2
width(7)
color("purple")
penup()
goto(80,0)
pendown()

forward(45)

exitonclick()
