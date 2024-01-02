import turtle

t = turtle.Turtle()
t.ht()
t.width(2)
turtle.tracer(2, 0)
window = turtle.Screen()
window.bgcolor('black')
t.color('yellow')
t.left(90)

t.penup()
t.setpos(0, -300)
t.pendown()


ln = 7
c = 10
#angle = 30
start = '0'
new_str = ''
stac = []
voc = {'1':'21', '0':'1[0]0'}


for i in range(c):
	for n in start:
		if n in voc:
			new_str += voc[n]
		else:
			new_str += n
	start = new_str
	new_str = ''



for a in start:
	if a == '1':
		t.forward(ln)
	elif a == '0':
		t.forward(ln)
	elif a == '2':
		t.forward(ln*2)
	elif a == '[':
		stac.append(t.xcor())
		stac.append(t.ycor())
		stac.append(t.heading())
		t.left(20)
	elif a == ']':
		t.penup()
		t.setheading(stac.pop())
		t.sety(stac.pop())
		t.setx(stac.pop())
		t.pendown()
		t.right(45)

turtle.done()