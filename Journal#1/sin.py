import math
import numpy as np
#create sin dunction
def sin_value():
    values=np.linspace(0,2 * np.pi,1000)
    sin_x=np.sin(values)

    return list(zip(values,sin_x))
#create table
def print_table(values):
    print("x    |sin(x) ")
    print("-------------")
    for x, sin_x in values:
        print(f"{x:.3f}|{sin_x:.3f}")

def main():
    values=sin_value()
    return print_table(values)

if __name__=="__main__":
    main()
