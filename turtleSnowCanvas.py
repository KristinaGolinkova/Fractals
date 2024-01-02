import turtle, random

t = turtle.Turtle()
t.ht()
window = turtle.Screen()
window.bgcolor('#050a14')
window.screensize(1500, 700)
t.color("#ffffb3")
turtle.tracer(0)


def draw_segment(str, lens, angle):
	for a in str:
		if a == 'F':
			t.forward(lens)
		elif a == '+':
			t.left(angle)
		elif a == '-':
			t.right(angle)

def draw_snow():
	ln = 200
	f = 'F'
	c = 1

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


def draw_line(x, y):
	for i in range(5):
		t.penup()
		t.setpos(x, y)
		t.pendown()
		draw_snow()
		y = y - 190

x = -750
y1 = 350
y2 = 445
for i in range(9):
	if i % 2 == 0:
		draw_line(x, y1)
		x = x + 164
	else:
		draw_line(x, y2)
		x = x + 164
turtle.done()

