from turtle import*

#we want to paint house
width(8)
speed(5)
shape("turtle")
color("orange")
begin_fill()
forward(300)
right(90)

forward(300)
right(90)

forward(300)
right(90)

forward(300)
right(90)
end_fill()
#end of the square

#drawing a door
penup()
goto(100, -300)
pendown()

color("red")
begin_fill()
left(90)
forward(150)
right(90)
forward(100)
right(90)
forward(150)
end_fill()

#end of the door

#painting the roof

begin_fill()
penup()
goto(300, 0)
pendown()
color("red")
begin_fill()

right(150)
forward(250)
left(110)
forward(280) 
 
end_fill()
#end of the roof

#painting windows
penup()
goto(30, -120)
pendown()
color("yellow")
begin_fill()
right(140)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()

penup()
goto(270, -120)
pendown()
color('yellow')
begin_fill()
right(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
end_fill()
#end of the window

#i want to paint field
penup()
goto(0, -300)
pendown()
speed(20)
color("green")
begin_fill()
forward(800)
left(180)
forward(1600)
left(90)
forward(100)
left(90)
forward(1600)
left(90)
forward(100)
end_fill()
exitonclick()