import turtle, random

t = turtle.Turtle()
t.ht()
turtle.tracer(0)
t.color('black')
t.left(90)
thick = 16
t.pensize(thick)

t.penup()
t.setpos(0, -350)
t.pendown()


ln = 10
c = 13
angle = 20
start = '222222220'
new_str = ''
stac = []
voc = {'1':'21', '0':'1[20]20'}


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
		if random.randint(0,10)>4:
			t.forward(ln)
	elif a == '0':
		stac.append(t.pensize())
		t.pensize(4)
		r = random.randint(0,10)
		if r < 3:
			t.pencolor('#F08080')
		elif r > 6:
			t.pencolor('#FFB6C1')
		else:
			t.pencolor('#DB7093')
		t.forward(ln*0.75)
		t.pensize(stac.pop())
		t.pencolor('black')
	elif a == '2':
		if random.randint(0,10)>4:
			t.forward(ln)
	elif a == '[':
		thick *= 0.75
		t.pensize(thick)
		stac.append(thick)
		stac.append(t.xcor())
		stac.append(t.ycor())
		stac.append(t.heading())
		t.left(angle + random.randint(-13,13))
	elif a == ']':
		t.penup()
		t.setheading(stac.pop())
		t.sety(stac.pop())
		t.setx(stac.pop())
		thick = stac.pop()
		t.pensize(thick)
		t.pendown()
		t.right(angle - random.randint(-13,13))

turtle.done()