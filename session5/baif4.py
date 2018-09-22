from turtle import*

shape("turtle")
speed(0)

loop = True
while loop :
    try:
        R = float(input("Nhập bán kính đường tron  ")) 
        circle(R)
    except ValueError:
        pass
mainloop()