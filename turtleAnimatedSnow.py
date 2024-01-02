import turtle, random

t = turtle.Turtle()
t.ht()
window = turtle.Screen()
window.bgcolor('#050a14')
window.screensize(1500, 700)
t.color("black", "white")
turtle.tracer(2, 0)


def draw_segment(str, lens, angle):
	for a in str:
		if a == 'F':
			t.forward(lens)
		elif a == '+':
			t.left(angle)
		elif a == '-':
			t.right(angle)

def draw_snow():
	t.left(random.randint(10,350))
	ln = random.randint(30,110)
	f = 'F'
	c = random.randint(1, 4)

	for i in range(c):
		f = f.replace('F', 'F+F--F+F')
		ln = ln // 3

	t.begin_fill()
	draw_segment(f, ln, 60)
	t.right(120)
	draw_segment(f, ln, 60)
	t.right(120)
	draw_segment(f, ln, 60)
	t.right(120)
	t.end_fill()

def move(x, y):
	t.penup()
	t.setpos(x, y)
	t.pendown()
	draw_snow()

window.onclick(move)
window.listen()
turtle.mainloop()

