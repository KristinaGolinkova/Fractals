import turtle

t = turtle.Turtle()
t.ht()
t.width(2)
turtle.tracer(3, 0)
window = turtle.Screen()
window.bgcolor('black')
t.color('yellow')

t.penup()
t.setpos(-150, -150)
t.pendown()

ln = 3
c = 15
angle = 90
f = 'FX'
new_str = ''
voc = {'+':'+', '-':'-', 'F':'F', 'X':'X+YF+', 'Y':'-FX-Y'}


for i in range(c):
	for letter in f:
		new_str += voc[letter]
	f = new_str
	new_str = ''


for a in f:
	if a == 'F':
		t.forward(ln)
	elif a == '+':
		t.right(angle)
	elif a == '-':
		t.left(angle)


turtle.done()