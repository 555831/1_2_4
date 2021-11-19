import turtle as trtl

maze_painter = trtl.Turtle()
maze_painter.hideturtle()

length = 20
pathwidth = 10
maze_painter.pensize(5)
maze_painter.penup()
maze_painter.forward(length)
maze_painter.pendown()
for i in range(25):
  maze_painter.left(90)
  maze_painter.forward(length/2)
  maze_painter.penup()
  maze_painter.forward(pathwidth*2)
  maze_painter.pendown()
  maze_painter.forward(length/2)

  length = length + 20

wn = trtl.Screen()
wn.mainloop()