# from physics import main
class equations:
    constantA = [["x2 = x0 + v1 * t1 + 0.5 * a1 * (t*t)",["x2","x1","v1","t1","a1"]], #constant acceleration
    ["x2 = x1 + 0.5 * (v2 + v1) * (t*t)",["x2","x1","v1","t1","v2"]],
    ["v2*v2 = (v1*v1) + 2 * a1 * (x2 * x1)",["v2","v1","a1","x2","x1"]],
    ["v2 = v1 + a * (t2 - t1)",["v2","v1","a1","t2","t1"]]]

    constantV = [["v1 = (x2 - x1)/(t2-t1)",["x2","x1","v1","t2","t1"]],
    ["x2 = x1 + v1 * (t2 - t1)",["x2","x1","v1","t2","t1"]]]

    constantJ = [["j = (a2 - a1) / (t2 - t1)",["j","a2","a1","t2","t1"]],
    ["x2 = v1 * (t2 - t1) + 0.5 * a1 * (t2 - t1)**2 + 1/6 * j * (t2 - t1)**3 + x1",["x2","v1","t2","t1","a1","j","x1"]]]
