import turtle

t = turtle.Turtle()
t.ht()
t.width(2)
window = turtle.Screen()
window.bgcolor('black')
t.color('yellow')

ln = 700
f = 'F'
rule = 'F+F--F+F'
c = 4

t.penup()
t.setpos(-250, 180)
t.pendown()

def draw(str, lens, angle):
	turtle.tracer(2, 0)
	for a in str:
		if a == 'F':
			t.forward(lens)
		elif a == '+':
			t.left(angle)
		elif a == '-':
			t.right(angle)

for i in range(c):
	f = f.replace('F', rule)
	ln = ln // 3

draw(f, ln, 60)
t.right(120)
draw(f, ln, 60)
t.right(120)
draw(f, ln, 60)
t.right(120)

turtle.done()

