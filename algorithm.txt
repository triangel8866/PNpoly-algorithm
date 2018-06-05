#polygon algorithm
flag = False
#for each point; p is port location, poly is eca areas
def raycasting(p,poly):
    for i in range(0,(len(poly) - 1)):
        j = i + 1
        sx = poly[i].Lattitude
        sy = poly[i].Longitude
        tx = poly[j].Lattitude
        ty = poly[j].Longitude

        #polygon points concide with ports location
        if ((sx == p.Lattitude & sy == p.Longitude) or (tx == p.Lattitude & ty == p.Longitude)):
            flag = True

        #points within two poly points y axis
        if ((p.Longitude < ty and p.Longitude > sy) or (p.Longitude < sy and p.Longitude > ty)):
            #points on straight line
            x = sx + (py - sy)*(ty - sy)/(tx - sy)

        #points on the line
        if x == p.Lattitude:
            flag = True

        #raycasting line
        if x > p.Lattitude:
            flag = !flag

    return flag
