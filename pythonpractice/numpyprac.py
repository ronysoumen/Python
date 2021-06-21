import numpy as np
value=80
grades=np.array([72, 35, 64, 88, 51, 90, 74, 12])
def curve(grades):
    avg=grades.mean()
    change=value-avg
    new_grades=grades+change
    print(new_grades)
    print(np.clip(new_grades,grades,100))
curve(grades)