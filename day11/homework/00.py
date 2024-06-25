from turtle import*
import turtle

turtle.pencolor("red")
speed(0)
bgcolor("black")

# forward(20)
# penup()
# goto(-380, -50)
# pendown()

def lines():
    penup()
    goto(-385, -150)
    pendown()
    color("green")
    right(75)
    forward(300000000000)

    penup()
    goto(-385, 50)
    pendown()
    forward(300000000)

    penup()
    goto(-385, 150)
    pendown()
    forward(3000000)

    penup()
    goto(-385, 250)
    pendown()
    forward(3000000)

    penup()
    goto(-385, 350)
    pendown()
    forward(3000000)

    penup()
    goto(100, 346)
    pendown()
    forward(30000000)

    penup()
    goto(164, 87)
    pendown()
    forward(300000000)

    penup()
    goto(2, 346)
    pendown()
    forward(3000000)


   

lines()

lines()

lines()

lines()

lines()

lines()

lines()

lines()

#first and last

penup()
goto(-150, 100)
pendown()
color("white")
begin_fill()
    

left(60)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(180)
forward(20)
left(90)
end_fill()

#2
penup()
goto(-135, 80)
pendown()
begin_fill()

forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(20)
left(180)
left(90)
end_fill()

#3
penup()
goto(-185, 80)
pendown()
begin_fill()


forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(180)
left(270)
end_fill()

#4
penup()
goto(-240, 80)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    left(90)
end_fill()

#5
penup()
goto(-240, 70)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    right(90)
end_fill()

#6
penup()
goto(-240, 37)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    right(90)

end_fill()

#7
penup()
goto(-240, 5)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    right(90)

end_fill()

#8
penup()
goto(-240, -25)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    right(90)
end_fill()

#9
penup()
goto(-135, -45)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    left(90)
end_fill()

#10
penup()
goto(-205, -45)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    left(90)
end_fill()

#11
penup()
goto(-170, -45)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    left(90)
end_fill()
#12
penup()
goto(-240, -45)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    left(90)
end_fill()
#13
penup()
goto(-135, 5)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    right(90)
end_fill()
#14
penup()
goto(-135, 37)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    right(90)
end_fill()
#15
penup()
goto(-170, 37)
pendown()
begin_fill()

for i in range(4):
    forward(20)
    right(90)
end_fill()


#drawing squared shape O

penup()
goto(-100, 20)
pendown()
turtle.pencolor("light green")


left(90)
forward(80)

for i in range(3):
    right(90)
    forward(145)
right(90)
forward(65)


#drawing inside of circle
penup()
goto(9, -7)
pendown()

for i in range(4):
    forward(73)
    left(90)

#drawing contures
left(223)
forward(54)

penup()
goto(9, 66)
pendown()

left(90)
forward(52)


penup()
goto(-65, 66)
pendown()

left(92)
forward(50)

penup()
goto(-65, -8)
pendown()

left(92)
forward(50)
#drawing A
penup()
goto(75,-45)
pendown()
left(133)

pencolor("white")
for i in range(4):
    forward(30)
    left(90)
end_fill()
begin_fill()
    
forward(30)
left(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)



right(90)

forward(30)
right(90)
forward(30)
right(90)
forward(60)
left(90)
forward(30)



left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)


right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)

right(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)



left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
left(90)
forward(30)



left(90)
forward(30)
right(90)
forward(45)
left(90)
forward(30)
left(90)
forward(155)


left(90)
forward(30)
end_fill()


penup()
goto(230, 145)
pendown()

left(90)

color("moccasin")
circle(15)
penup()
goto(245,130)


exitonclick()