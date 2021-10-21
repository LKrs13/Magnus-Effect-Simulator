from vpython import *


scene.userzoom=True
scene.width = 1920
scene.height = 1080
#graphs
thegraph=graph(title="Position en fonction du temps", xtitle="Temps [s]", ytitle="Position [m]", fast=True)
fA=gcurve(color=color.blue, label="Position X")
fB=gcurve(color=color.red,label="Position Y")
fC=gcurve(color=color.green,label="Position Z")

graph2=graph(title="Position Y en fonction de la position X", xtitle="Position X [m]", ytitle="Position Y [m]", fast=True)
pos1=gcurve(color=color.blue, label="Position X")

graph3=graph(title="Vitesse en fonction du temps", xtitle="Temps [s]", ytitle="Vitesse [m/s]", fast=True)
gV1=gcurve(color=color.purple, label="Vitesse")
gVx=gcurve(color=color.blue, label="Vitesse X")
gVy=gcurve(color=color.red,label="Vitesse Y")
gVz=gcurve(color=color.green,label="Vitesse Z")

#gravitational field vector
g=vector(0,-9.8,0)

#ground & field
ground=box(pos=vector(0,-1.5,0), size=vector(65,.2,36), color=color.green)
line=box(pos=vector(0,-1.49,0), size=vector(.1,.2,36), color=color.white)
skel1 = cylinder(pos = vector(3.66, -1.5, -18), axis = vector(0.1, 4, 0.1), radius = 0.3)
skel2 = cylinder(pos = vector(-3.66, -1.5, -18), axis = vector(0.1, 4, 0.1), radius = 0.3)
skel3 = cylinder(pos = vector(-3.85, 2.44, -18), axis = vector(7.8, 0.1, 0.1), radius = 0.3)
whole = compound([skel1, skel2, skel3]) # body of crossbar

#ball
ball=sphere(pos=vector(0,-1.4,18.5), radius=.105, color=color.white, make_trail=True)
#density of soccer ball
rhosoccer=74*1.02 #74 times the density of air
#mass of the soccer ball
ball.m= .43

#Angular velocity of ball
ball.omega=vector(-25,88,0)

ball2=sphere(pos=ball.pos, radius=ball.radius, color=color.yellow, make_trail=True)

#launch speed in m/s 
v0=44
#launch angle
theta = 15*pi/180

#initial velocity vector
ball.v=v0*vector(.40,sin(theta),-cos(theta))
#initial momentum vector
ball.p=ball.m*ball.v

ball2.p=ball.p
ball2.m=ball.m

rho=1.02 #density of air
C=.15 #the drag coefficient for a sphere
A = pi*ball.radius**2
s=.0033 #this is a magnus force constant

t=0
dt=0.001

while ball.pos.z>=-18.5:
    rate(1000)
    #scene.camera.follow(ball)
    #calculate the velocity- it makes it easier to calc air drag
    ball.v=ball.p/ball.m
   #calculate the force
   #note that to square velocity, must first find magnitude
   #in order to make it a vector, I multiply by unit vector for v
    F=ball.m*g-.5*rho*A*C*norm(ball.v)*mag(ball.v)**2+s*cross(ball.omega,ball.v)
    F2=ball2.m*g
    #update the momentum
    ball.p=ball.p+F*dt
    ball2.p=ball2.p+F2*dt
    #update the position
    ball.pos=ball.pos+ball.p*dt/ball.m
    ball2.pos=ball2.pos+ball2.p*dt/ball2.m
    #update the time
    t=t+dt
    fA.plot(t, ball.pos.z)
    fB.plot(t, ball.pos.x)
    fC.plot(t, ball.pos.y)
    gV1.plot(t, mag(ball.v))
    gVx.plot(t, abs(ball.v.z))
    gVy.plot(t, ball.v.y)
    gVz.plot(t, ball.v.x)
    pos1.plot(ball.pos.z, ball.pos.x)