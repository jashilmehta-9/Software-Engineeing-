def classifyTriangle(x,y,z):
    if (x>100 or y>100 or c>100):
        return 'triangle not valid'

    if x<=0 or y<=0 or z<=0:
        return 'triangle not valid'
    
    if x==y and y==z:
        return 'Equilatertal traiangle'
    elif ((x*x) + (y*y)) == (z*z) or ((z*z) + (y*y)) == (x*x) or ((x*x) + (z*z)) == (y*y):
        return 'Right Angle triangle'
    elif x==y or y==z or x==z:
        return 'Isocles Traingle'
    else: 
        return 'Scalene Trainagle'