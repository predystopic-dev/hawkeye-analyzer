#Web VPython 3.2
from vpython import *

scene = canvas(title='Phys 2211K Lab 1', width=1000, height=800, center=vector(0,0,0), background=color.white)

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""


# wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
# wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
pitch = box (pos=vector(0, -4, 0), size=vector(22.12, 0.01, 3.05),  color = vector(0.94,0.9,0.8))
# wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
# wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))



ball = sphere(radius=0.071, color=color.red, make_trail=True, trail_color=color.red) 
ball.mass = 0.16
ball.pos = vector(-11.06, -2.0, 0.0)
x = 4.0
z = 1
y = -4
dt = 0.3


run = False
def pause(b):
    global run
    run = not run
    if run: b.text = 'Pause'
    else: b.text = 'Run'
button(text='Run', bind=pause)

while True:
    rate(200)
    if not run: continue
    #ball.pos = ball.pos + (ball.pos/ball.mass)*dt
    ball.pos.x = x
    ball.pos.y = y
    #    ball.velocity = ball.velocity + vector(0,-9.8,0)*dt
