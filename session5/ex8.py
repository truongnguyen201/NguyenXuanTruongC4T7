from turtle import*

shape("turtle")
speed(0)

n = int(input("Nhập 1 số:   "))
for i in range(n):
    forward(90)
    left(360/n)

mainloop()