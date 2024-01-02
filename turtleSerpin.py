import turtle

t = turtle.Turtle()
t.ht()
t.width(2)
turtle.tracer(2, 0)
window = turtle.Screen()
window.bgcolor('black')
t.color('yellow')

t.penup()
t.setpos(-350, -300)
t.pendown()

ln = 1.5
c = 9
angle = 60
start = 'A'
new_str = ''
voc = {'+':'+', '-':'-', 'A':'B-A-B', 'B':'A+B+A'}


for i in range(c):
	for n in start:
		new_str += voc[n]
	start = new_str
	new_str = ''


for a in start:
	if a == 'A' or a == 'B':
		t.forward(ln)
	elif a == '+':
		t.right(angle)
	elif a == '-':
		t.left(angle)

turtle.done()