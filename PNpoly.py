def raycasting(p,poly):
    flag = False
    for i in range(0,(len(poly) - 1)):
        j = i + 1
        sx = poly['Latitude'][i]
        sy = poly['Longitude'][i]
        tx = poly['Latitude'][j]
        ty = poly['Longitude'][j]

        x = np.NaN
        #points within two poly points y axis
        if ((p.Longitude < ty and p.Longitude > sy) or (p.Longitude < sy and p.Longitude > ty)):
            #points on straight line
            x = sx + (ty - sy)*(ty - sy)/(tx - sy)

            #points on the line
        if x == p.Latitude:
            flag = True

        #raycasting line
        if x > p.Latitude:
            flag = not flag

        #polygon points concide with ports location
        if ((sx == p.Latitude and sy == p.Longitude) or (tx == p.Latitude and ty == p.Longitude)):
            flag = True

    return flag


