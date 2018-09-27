#polygon algorithm
def raycasting(p,poly):
    #for each point; p is port location, poly is eca areas
    flag = False
    polygon = tuple(poly[:])+(poly[0],)
    for i in range(0,(len(polygon) - 1)):
        j = i + 1
        sx = polygon[i]['Latitude']
        sy = polygon[i]['Longitude']
        tx = polygon[j]['Latitude']
        ty = polygon[j]['Longitude']

        x = np.NaN
        #points within two poly points y axis
        if ((p[1] < ty and p[1] > sy) or (p[1] < sy and p[1] > ty)):
            #points on straight line
            x = sx + (p[1] - sy)*(tx - sx)/(ty - sy)

        #points on the line
        if x == p[0]:
            flag = True

        #raycasting line
        if x > p[0]:
            flag = not flag

        #polygon points concide with ports location
        if ((sx == p[0] and sy == p[1]) or (tx == p[0] and ty == p[1])):
            flag = True

    return flag


