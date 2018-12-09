def is_square(a, b, c, d):
    distance = []
    distance1 = (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])
    distance2 = (a[0]-c[0])*(a[0]-c[0]) + (a[1]-c[1])*(a[1]-c[1])
    distance3 = (a[0]-d[0])*(a[0]-d[0]) + (a[1]-d[1])*(a[1]-d[1])
    distance4 = (b[0]-c[0])*(b[0]-c[0]) + (b[1]-c[1])*(b[1]-c[1])
    distance5 = (b[0]-d[0])*(b[0]-d[0]) + (b[1]-d[1])*(b[1]-d[1])
    distance6 = (d[0]-c[0])*(d[0]-c[0]) + (d[1]-c[1])*(d[1]-c[1])

    distance.append(distance1)
    distance.append(distance2)
    distance.append(distance3)
    distance.append(distance4)
    distance.append(distance5)
    distance.append(distance6)

    unique = set(distance)

    if not len(unique) == 2:
        return False
    else:
        return min(unique)*min(unique) + min(unique)*min(unique)== max(unique)*max(unique)


print(is_square([1,2], [3,4], [3,5], [2,6]))



