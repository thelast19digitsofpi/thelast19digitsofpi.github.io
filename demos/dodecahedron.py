# generates the dodecahedral stereographic projection used on the result cards

# some maths:
# ICOSAHEDRON vertices are (0,0,1), (0,0,-1), and ten points with angle-with-z-axis arctan(1/2)
# so we have (r*cos(theta), r*sin(theta), z) where r = 1/sqrt(5), z = 2/sqrt(5)
# DODECAHEDRON vertices can be defined as the spherical averages of trios of adjacent points.

from math import *
SQRT5 = 5 ** 0.5

# Spherical Linear Interpolation
def slerp(p1, p2, t):
    lerp = tuple(p1[i]*(1-t) + p2[i]*t for i in range(3))
    norm = sum(u**2 for u in lerp)**0.5
    return tuple(u/norm for u in lerp)

# for dodecahedron I also need centers of triangles
def scenter(p1, p2, p3):
    e_mid = tuple((p1[i]+p2[i]+p3[i])/3 for i in range(3))
    norm = sum(u**2 for u in e_mid)**0.5
    return tuple(u/norm for u in e_mid)

# Stereographic Projection
def stereo(p):
    return (p[0]/(1 - p[2]), p[1]/(1 - p[2]))

# Arc from p1 to p2
def arc(p1, p2, n, scale):
    xy1 = stereo(p1)
    output = "M{:.1f},{:.1f}".format(xy1[0] * scale, xy1[1] * scale)
    for i in range(1,n+1):
        try:
            xy = stereo(slerp(p1, p2, i/n))
            output += " L{:.1f},{:.1f}".format(xy[0] * scale, xy[1] * scale)
        except ZeroDivisionError:
            pass
    return output.replace(".0", "")

def dodecahedron(scale):
    paths = []
    
    # icosahedron points
    north_pole = (0,0,1)
    icos_near_north = []
    icos_near_south = []
    south_pole = (0,0,-1)
    
    # it's a little complicated to fill the other ten icosahedron points
    z = 1/SQRT5
    for i in range(5):
        theta_north = 2 * pi * i/5
        theta_south = 2 * pi * (i+0.5)/5
        icos_near_north.append((cos(theta_north) * 2/SQRT5, sin(theta_north) * 2/SQRT5, z))
        icos_near_south.append((cos(theta_south) * 2/SQRT5, sin(theta_south) * 2/SQRT5, -z))

    # dodecahedron vertices are based on the icosahedron ones
    ring1 = []
    ring2 = []
    ring3 = []
    ring4 = []
    for i in range(5):
        ring1.append(scenter(north_pole, icos_near_north[i-1], icos_near_north[i]))
        ring2.append(scenter(icos_near_north[i-1], icos_near_north[i], icos_near_south[i-1]))
        ring3.append(scenter(icos_near_south[i-1], icos_near_south[i], icos_near_north[i]))
        ring4.append(scenter(south_pole, icos_near_south[i-1], icos_near_south[i]))
    
    # ok, now we're ready
    for i in range(5):
        n = 8
        paths.append(arc(ring1[i-1], ring1[i], n*3, scale))
        paths.append(arc(ring1[i], ring2[i], 1, scale))
        paths.append(arc(ring2[i], ring3[i], n, scale))
        paths.append(arc(ring2[i], ring3[i-1], n, scale))
        paths.append(arc(ring3[i], ring4[i], 1, scale))
        paths.append(arc(ring4[i-1], ring4[i], n//2, scale))
    
    # convert and ship
    return "\n".join("<path d=\"" + d + "\" />" for d in paths)
    

scale = float(input("Enter a scale: "))
print("\n\n")
print(dodecahedron(scale))



