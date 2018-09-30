from turtle import*

shape('turtle')
speed(0)
for i in range(4):
    forward(20)
    if i == 0:
        color('blue')
    elif i == 1:
        color('red')
    elif i == 2:
        color('teal')
    elif i == 3:
        color('green')


mainloop()