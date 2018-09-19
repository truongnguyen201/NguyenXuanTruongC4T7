from turtle import*

shape("turtle")

a = 3


for i in range(4):
    if a%2 == 0:
        color("red")
    else:
        color("blue")
    
    b = 360/a
    for j in range(a):
        forward(90)
        left(b)
       
    
    a = a +1
       


mainloop()