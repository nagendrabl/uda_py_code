import turtle


window = turtle.Screen()
window.bgcolor("red")
                    
icon = turtle.Turtle()
icon.color("blue")
icon.shape("turtle")

def draw_square(z):
    n=0       
    while (n<4):
        icon.forward(z)
        icon.rt(90)
        n=n+1

def draw_circle(n):
    icon.circle(n)

def draw_triangle(x,y,z):       
    icon.left(180)
    icon.forward(x)
    icon.rt(120)
    icon.forward(y)
    icon.rt(120)
    icon.forward(z)

deg=0;        
while  (deg < 361):           
    draw_square(100);
    deg=deg+10
    icon.rt(10);
